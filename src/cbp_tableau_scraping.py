# Import helper python libraries
from tableauscraper import TableauScraper as TS
import itertools
import logging
import time
import pprint
import pandas as pd

pp = pprint.PrettyPrinter(indent=4)


def find_filters_worksheet(ts):
    workbook = ts.getWorkbook()
    filters_ws = None
    wb_names = []
    for t in workbook.worksheets:
        filters = t.getFilters()
        if len(filters) > 0:
            print(
                f"Filters Presesnt on worksheet name --> {t.name}"
            )  # show worksheet name
            pp.pprint(filters)  # show dataframe for this worksheet
            filters_ws = t.name
        else:
            print("no filters", t.name)

        wb_names.append(t.name)
    return filters_ws, wb_names


def unpack_filter_information(ts, filters_ws):

    # Specifically ask for the Line Graph since it has the filters
    ws = ts.getWorksheet(filters_ws)

    # Get the different filter names and their values
    filter_master_list = ws.getFilters()
    filter_possible_values_list = {i["column"]: i["values"] for i in filter_master_list}

    # We hold this data in a dictionary and where the filter names are keys
    # and the values are lists of possible values
    pp.pprint(filter_possible_values_list)

    # Grab just the column names
    all_filter_columns = [i["column"] for i in filter_master_list]
    # Drop the fiscal year because the chart automatically includes all fiscal years
    try:
        all_filter_columns.remove("Fiscal Year")
    except ValueError:
        print("Fiscal year not present")

    # This is somewhat complicated, but what it does is creates an exhaustive
    # list of all possible filter combinations, this does not control for
    # combinations that don't exist though, meaning that some filter comnbinations
    # don't have any data in the chart. We will control for that next
    all_f_values = []
    for f in filter_master_list:
        if f["column"] != "Fiscal Year":
            vals = f["values"]
            all_f_values.append([None] + vals)
    all_filter_combinations = list(itertools.product(*all_f_values))

    filter_data = {
        "master_list": filter_master_list,
        "filter_columns": all_filter_columns,
        "filter_combinations": all_filter_combinations,
    }
    return filter_data


def get_dashboard_data(
    url, all_filter_columns, all_filter_combinations, filter_worksheet, data_worksheet
):
    failed_combination = []
    tableau_dataframe = pd.DataFrame()
    for filter_combination in all_filter_combinations:
        print("Attempting Fitler Combination", filter_combination)
        ts = TS()
        ts.loads(url)
        workbook = ts  # in case all filters are null
        worksheet = ts.getWorksheet(filter_worksheet)
        try:
            for idx, col in enumerate(all_filter_columns):
                # If it is none it means we are not applying any filter option for the dropdown filter
                if filter_combination[idx] is None:
                    continue
                else:
                    worksheet = workbook.getWorksheet(filter_worksheet)
                    workbook = worksheet.setFilter(
                        col, filter_combination[idx], filterDelta=True
                    )

            subset_worksheet = workbook.getWorksheet(data_worksheet)
            subset_data = subset_worksheet.data
            if len(subset_data) > 0:  # Only do this if we have data
                # Now we iterate over the fitler and label the data with
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
