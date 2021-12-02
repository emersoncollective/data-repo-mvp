# Import helper python libraries
import argparse
import itertools
import logging
import logging.config
import time

import pandas as pd
from tableauscraper import TableauScraper as TS

logging.config.dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": True,
    }
)


def find_filters_worksheet(ts):

    """
    Function to search the dashboard to find the worksheet that manages
    the filters that are available on the dashboard.
    """
    workbook = ts.getWorkbook()
    filters_ws = None
    wb_names = []
    for t in workbook.worksheets:
        filters = t.getFilters()
        if len(filters) > 0:
            print("-" * 90)
            print(
                f"Filters present on element name --> {t.name}"
            )  # show worksheet name
            filters_ws = t.name
            print("-" * 90)
        else:
            print("\nno filters found on element --> ", t.name)

        wb_names.append(t.name)
    return filters_ws, wb_names


def unpack_filter_information(ts, filters_ws, skip_filter=[]):

    """
    Function process filters and return object of information on those filters,
    on all the combinations, columns names, and other useful information.

    skip_filter: is a list with column names that should be skipped, you are likley
    skipping columns because the you do not need to apply that filter.

    returns dictionary
    """

    # Specifically ask for the Line Graph since it has the filters
    ws = ts.getWorksheet(filters_ws)

    # Get the different filter names and their corresponding options, then store this data in a dictionary,
    # where the filter names are keys and the values are lists of corresponding filter options
    filter_master_list = ws.getFilters()
    filter_possible_values_list = {i["column"]: i["values"] for i in filter_master_list}
    print("\nFilters and their possible values:")

    # Grab just the column names
    all_filter_columns = [i["column"] for i in filter_master_list]
    # Drop the fiscal year because the chart automatically includes all fiscal years
    for col in skip_filter:
        try:
            all_filter_columns.remove(col)
        except ValueError:
            print(f"{col} not present")

    # The code belew creates an exhaustive
    # list of all possible filter combinations, this does not control for
    # combinations that don't exist though, meaning that some filter comnbinations
    # that don't have any valid data may be attempted, this is fine though we just
    # won't get data back for those combinations.
    all_f_values = []
    for f in filter_master_list:
        if f["column"] not in skip_filter:
            vals = f["values"]
            all_f_values.append([None] + vals)
    all_filter_combinations = list(itertools.product(*all_f_values))

    filter_data = {
        "master_list": filter_master_list,
        "filter_columns": all_filter_columns,
        "filter_combinations": all_filter_combinations,
    }
    print("\nFilter on:")
    return filter_data


def get_dashboard_data(
    url: str,
    all_filter_columns: list,
    all_filter_combinations,
    filter_worksheet,
    data_worksheet,
):
    """
    @param url: url of dashboard
    @param all_filter_columns: list of columns we will use for filtering
    @param all_filter_combinations: list of tuples containing all filter combinations
    @param filter_worksheet: worksheet where filters exist
    @param data_worksheet: worksheet we want to extract data from

    return dashboard data extracted from tableau dashboard element
    """
    failed_combination = []
    tableau_dataframe = pd.DataFrame()
    for filter_combination in all_filter_combinations:
        print("Attempting Filter Combination", filter_combination)
        for attempt in range(10):
            try:
                ts = TS()
                ts.loads(url)
                time.sleep(5)
                workbook = ts  # in case all filters are null
                worksheet = ts.getWorksheet(filter_worksheet)
                break  # if gotten this far i think i'm successful
            except Exception as e:
                print(f"Error on attempt: {attempt}\n", e)
        try:
            for idx, col in enumerate(all_filter_columns):
                # If it is none it means we are not applying any filter option for the dropdown filter
                if filter_combination[idx] is None:
                    continue
                else:
                    # apply the individual filter and continue iterating
                    worksheet = workbook.getWorksheet(filter_worksheet)
                    workbook = worksheet.setFilter(
                        col, filter_combination[idx], filterDelta=True
                    )
            subset_worksheet = workbook.getWorksheet(data_worksheet)
            subset_data = subset_worksheet.data
            if len(subset_data) > 0:  # Only do this if we have data
                # Now we iterate over the filter and label the data with
                # what filters were applied.
                for col, val in list(zip(all_filter_columns, filter_combination)):
                    if val is None:
                        val = "all"
                    subset_data.loc[:, col] = val

                # append the data to our master dataframe
                tableau_dataframe = tableau_dataframe.append(subset_data)
            else:
                print(f"WARNING No Length on {filter_combination}")
                failed_combination.append(filter_combination)
        except Exception as e:
            print(f"WARNING on {filter_combination} \n {e}")
            failed_combination.append(filter_combination)
    return tableau_dataframe, failed_combination


if __name__ == "__main__":

    # dashboard1_url = "https://publicstats.cbp.gov/t/PublicFacing/views/CBPSBOEnforcementActionsDashboardsOCTFY22/SBOEncounters10935"
    # dashboard2_url = "https://publicstats.cbp.gov/t/PublicFacing/views/CBPSBOEnforcementActionsDashboardsOCTFY22/SBObyMonthDemo10935"

    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser(description="Which url to process")
    parser.add_argument("--url")
    parser.add_argument("--data_element")
    parser.add_argument("--skip_filters")
    parser.add_argument("--label")
    args = parser.parse_args()

    dashboard_url = args.url
    skip_filters = eval(args.skip_filters)

    # Run process
    ts = TS()
    ts.loads(dashboard_url)
    data_element_target = args.data_element
    filters_ws, wb_names = find_filters_worksheet(ts)

    # Dashboard 1- Note we skip fiscal year because it is broken out in the chart already
    filter_data = unpack_filter_information(
        ts,
        filters_ws,
        skip_filter=skip_filters,
    )

    dataset, failed_combination = get_dashboard_data(
        dashboard_url,
        filter_data["filter_columns"],
        filter_data["filter_combinations"],
        filters_ws,
        data_element_target,
    )
    today_date = time.strftime("%Y-%m-%d")
    print("Failed Combinations")
    print(len(failed_combination))
    print(failed_combination)

    dataset.to_csv(f"./data/extracted_data/cbp-tableau/{args.label}-{today_date}.csv")
