# Import helper python libraries
import argparse
import datetime
import itertools
import logging
import logging.config
import os
import time
import urllib
from pathlib import Path
from urllib.parse import unquote

import pandas as pd
import requests
from bs4 import BeautifulSoup
from tableauscraper import TableauScraper as TS

import logger
from utils import are_files_identical, get_date_from_filename

logging.config.dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": True,
    }
)

OUTPUT_DIRECTORY = Path("./data/extracted_data/cbp-tableau")


class CBPTableauScraper:
    """
    TODO
    """

    def __init__(self, custom_logger, args):
        self.custom_logger = custom_logger
        self.args = args

    @staticmethod
    def get_tableau_dashboard_url_from_tableau_placeholder(item):
        """
        Takes an item with a class of tableauPlaceholder and returns a valid url for a dashboard

        Parameters:
            item: Beautiful soup item with class of tableauPlaceholder

        Returns:
            A valid url for a Tableau dashboard
        """
        url = unquote(item.find("param", {"name": "host_url"})["value"]).strip("/")
        url += (
            "/"
            + unquote(item.find("param", {"name": "site_root"})["value"]).strip("/")
            + "/views"
        )
        url += "/" + unquote(item.find("param", {"name": "name"})["value"]).strip("/")
        return url

    def get_dashboard_urls(self):
        # Below we take the URL of the CPB webpage, and search for tableaPlaceholder elements in the
        # webpage background information.
        url = "https://www.cbp.gov/newsroom/stats/southwest-land-border-encounters"
        request = requests.get(url)  # get the URL's data
        soup = BeautifulSoup(request.text, "html.parser")  # parse it with Beautifulsoup

        # Find the tableauPlaceholder divs and get the dashboard URLs
        print("Getting URLs")
        urls = {}
        for idx, item in enumerate(
            soup.find_all("div", {"class": "tableauPlaceholder"})
        ):
            retrieved_url = self.get_tableau_dashboard_url_from_tableau_placeholder(
                item
            )
            print(idx + 1, retrieved_url)
            urls[idx + 1] = retrieved_url
        return urls

    def get_last_modified_date(self):
        url = "https://www.cbp.gov/newsroom/stats/southwest-land-border-encounters"
        page = requests.get(url)
        html = page.text
        soup = BeautifulSoup(html, "lxml")

        last_modified_date = (
            [
                i
                for i in soup.select('div[class="field-label"]')
                if "last modified" in i.text.lower()
            ][0]
            .find_next("div")
            .text
        )
        return "_".join(last_modified_date.lower().replace(",", "").split(" "))

    def find_filters_worksheet(self, ts):

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
                self.custom_logger.info(
                    f"Filters present on element name --> {t.name}"
                )  # show worksheet name
                filters_ws = t.name
            else:
                self.custom_logger.info("\nno filters found on element --> " + t.name)

            wb_names.append(t.name)
        return filters_ws, wb_names

    def unpack_filter_information(self, ts, filters_ws, skip_filter=[]):

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
        filter_possible_values_list = {
            i["column"]: i["values"] for i in filter_master_list
        }

        # Grab just the column names
        all_filter_columns = [i["column"] for i in filter_master_list]
        # Drop the fiscal year because the chart automatically includes all fiscal years
        for col in skip_filter:
            try:
                all_filter_columns.remove(col)
            except ValueError:
                self.custom_logger.info(f"{col} not present")

        # The code below creates an exhaustive
        # list of all possible filter combinations, this does not control for
        # combinations that don't exist though, meaning that some filter combinations
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
        return filter_data

    def get_dashboard_data(
        self,
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
        filter_count = 0
        for filter_combination in all_filter_combinations:
            # self.custom_logger.info("Attempting Filter Combination", filter_combination)
            for attempt in range(15):
                try:
                    filter_count += 1
                    ts = TS()
                    ts.loads(url)
                    time.sleep(1)
                    workbook = ts  # in case all filters are null
                    worksheet = ts.getWorksheet(filter_worksheet)
                    self.custom_logger.info(
                        f"On filter #{filter_count} / {len(all_filter_combinations)}"
                    )

                    for idx, col in enumerate(all_filter_columns):
                        # If it is none it means we are not applying any filter option for the dropdown filter
                        if filter_combination[idx] is None:
                            continue
                        else:
                            # apply the individual filter components and continue iterating
                            worksheet = workbook.getWorksheet(filter_worksheet)
                            workbook = worksheet.setFilter(
                                col, filter_combination[idx], filterDelta=True
                            )

                    subset_worksheet = workbook.getWorksheet(data_worksheet)
                    subset_data = subset_worksheet.data
                    if len(subset_data) > 0:  # Only do this if we have data
                        # Now we iterate over the filter and label the data with
                        # what filters were applied.
                        for col, val in list(
                            zip(all_filter_columns, filter_combination)
                        ):
                            if val is None:
                                val = "all"
                            subset_data.loc[:, col] = val

                        # append the data to our master dataframe
                        tableau_dataframe = tableau_dataframe.append(subset_data)
                    else:
                        self.custom_logger.info(
                            f"WARNING No Length on {str(filter_combination)}"
                        )
                        failed_combination.append(filter_combination)

                    break  # if gotten this far i think i'm successful
                except Exception as e:
                    filter_count -= 1
                    # This is a quick fix since I'm not sure what else can be done
                    self.custom_logger.info(
                        f"Attempt {attempt+1} on filter combo: {str(filter_combination)}"
                    )
                    failed_combination.append(filter_combination)

        return tableau_dataframe, failed_combination

    def run(self):
        args = self.args
        # Get the dashboard specific urls - they are dynamic and can change
        urls = self.get_dashboard_urls()
        assert len(urls) > 0, "Urls not retrieved"
        dashboard_url = urls[int(args.dashboard_number)]
        skip_filters = eval(args.skip_filters)
        last_modified = self.get_last_modified_date()
        today = datetime.date.today().strftime("%B_%d_%Y").lower()
        run_label = args.label
        # Steps
        # check if we already have the file ...
        # tag the file with the date if it doesn't exists
        # if the

        output_file_label = f"{run_label}_official_update-{last_modified}.csv"
        output_file_path = OUTPUT_DIRECTORY / output_file_label
        check_for_change_run = False
        if output_file_path not in [f for f in OUTPUT_DIRECTORY.iterdir()]:
            self.custom_logger.info(
                "Official Update Occurred  - starting extraction ..."
            )
        else:
            check_for_change_run = True
            self.custom_logger.info("Processing to check for unofficial updates...")
            output_file_label = f"{run_label}_detected_change-{today}.csv"
            output_file_path = OUTPUT_DIRECTORY / output_file_label

        # Run process
        ts = TS()
        ts.loads(dashboard_url)
        data_element_target = args.data_element
        filters_ws, _ = self.find_filters_worksheet(ts)

        filter_data = self.unpack_filter_information(
            ts,
            filters_ws,
            skip_filter=skip_filters,
        )

        dataset, failed_combination = self.get_dashboard_data(
            dashboard_url,
            filter_data["filter_columns"],
            filter_data["filter_combinations"],
            filters_ws,
            data_element_target,
        )
        failed_combination = list(set([str(i) for i in failed_combination]))
        self.custom_logger.info("Failed Combinations")
        self.custom_logger.info(len(failed_combination))
        self.custom_logger.info(failed_combination)

        # save to disk
        dataset.to_csv(output_file_path, index=False)

        if check_for_change_run:
            # 1 - find the most recent file for this specific run label - not picking the file we just saved to disk
            files = [f.name for f in OUTPUT_DIRECTORY.iterdir()]
            files.remove(output_file_label)
            lastest_file = max(
                [(f, get_date_from_filename(f)) for f in files if run_label in f],
                key=lambda x: x[1],
            )
            # 2 - compare the newest file of that run label to the one we just created
            if are_files_identical(
                OUTPUT_DIRECTORY / lastest_file[0], output_file_path
            ):
                # 3 if the newest file is different than the one we just made - do nothing
                os.remove(output_file_path)
                custom_logger.info(
                    "File was identical to previous file - extract removed."
                )
            else:
                custom_logger.info("Change detected in file.")


if __name__ == "__main__":

    # dashboard1_url = "https://publicstats.cbp.gov/t/PublicFacing/views/CBPSBOEnforcementActionsDashboardsOCTFY22/SBOEncounters10935"
    # dashboard2_url = "https://publicstats.cbp.gov/t/PublicFacing/views/CBPSBOEnforcementActionsDashboardsOCTFY22/SBObyMonthDemo10935"

    parser = argparse.ArgumentParser(description="Which url to process")
    parser.add_argument("--dashboard_number")
    parser.add_argument("--data_element")
    parser.add_argument("--skip_filters")
    parser.add_argument("--label")
    args = parser.parse_args()
    # Logging
    custom_logger, LOG_FILE = logger.create_and_return_logger(
        f"cbp-tableau-scraper-{args.label}", filename=f"cbp_scraper_"
    )

    # Run the Procss
    custom_logger.info("## Starting ##")
    cbp_scraper = CBPTableauScraper(custom_logger, args)
    try:
        cbp_scraper.run()
    except Exception as e:
        custom_logger.exception(e)
        custom_logger.info("Execution Failed - See logs")
