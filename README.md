# The Immigration Data Repository 

## Background 
The Immigration Data Repo is powered by the Emerson Collective. This is a place where we post immigration related datasets that have been collected (typically by us). The data comes mostly from public sources. 

You can use this repository to datasets to use here, but to also...
* download the data
* get a sense of how the data was collected
* learn how to use, and adapt, code to procure and format immigration datasets from the web

**Have any questions?** Feel free to [get in touch with us!](#contact-us)

**Do you want to connect and engage with a community of trusted peers to learn from/with?** Feel free to [join our Slack Channel!]()

**Do you have any code or datasets you want to share with this community?** Feel free to [let us know!]((#contact-us))

<br>

## Getting Started 

### 1. Are you just looking for the data?
 
 See the [Data Inventory](#data-inventory) table below. The links in the **See Data** column will connect you to where the extracted data for that specific source is located. 
 * We update select datasets as new data gets released 
 <span style="color:red">**!! TBD - not yet true but hopefully soon!!**</span> 
 * Data outputs may be in the form of a single file or multiple files depending on the source. 

## Data Inventory 

|   | Dataset Name                                                                      | Source                          | Original URL                                                                              | See Data                                          | See Code                                                    | Updated Regularly? |
| - | --------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------- | ----------------------------------------------------------- | ------------------ |
| 1 | CBP Southwest Land Border Encounters                                              | CBP                             | [source](https://www.cbp.gov/newsroom/stats/southwest-land-border-encounters)             | [dataset ](data/extracted_data/cbp-tableau)       | [code](Notebooks/CBP-Encounters.ipynb)                      | Yes                |
| 2 | U.S. Border Patrol Nationwide Apprehensions by Citizenship and Sector FY2007-2020 | CBP                             | [source ](https://www.cbp.gov/sites/default/files/assets/documents/2021-Aug/USBORD~3.PDF) | [dataset ](data/extracted_data/cbp-apprehensions) | [code](Notebooks/CBP-Apprehensions.ipynb)                   | No                 |
| 3 | State Department Monthly Visa Issuances                                           | US State Department             | [source](https://travel.state.gov/content/travel/en/legal/visa-law0/visa-statistics.html) | [dataset ](data/extracted_data/state-dept)        | [code](notebooks/State-Dept-Monthly-Visa-Stats.ipynb)       | TBD                |
| 4 | EOIR Asylum Decision Rates by Nationality                                         | US Department of Justice / EOIR | [source](https://www.justice.gov/eoir/page/file/1107366/download)                         | [dataset ](data/extracted_data/doj)               | [code](notebooks/DOJ-Asylum-Decisions-by-Nationality.ipynb) | TODO               |
| 5 | USCIS Congressional Semi-Monthly Report (CFR/RFR)                                 | US State Department             | [source](https://travel.state.gov/content/travel/en/legal/visa-law0/visa-statistics.html) | TBD                                               | [code](Notebooks/USCIS-Credible-Fear-Spreadsheets.ipynb)    | TBD                |
| 6 | US Census Miscellaneous                                                           | US Census                       | [source](https://data.census.gov/cedsci/)                                                 | NA                                                | [code](notebooks/Census-Data.ipynb)                         | No                 |
| … | More to come                                                                      |                                 |                                                                                           |                                                   |                                                             |                    |

<br>

We recommend reviewing the code notebooks used to generate the data to allow for better understanding of how to extract such information and what the data structure will be. 

<br>

### 2. Would you like to review and run the code used to generate data? 
<br>
Fantastic! We have used code notebooks (called Jupyter Notebooks) to write Python code to extract the different datasets. The Notebooks are annotated to explain the methodology in a stepwise manner. We host the Notebooks on an interactive evironment (a JupyterHub) so that you can run the code yourself if you like! 

The environment has everything you need to run the code -- no need to install python and maintaining the environment on your computer. You can also write and run your own code on your JupyterHub.


#### **If you are new to Python, continue with the instructions [here](/learn_python.md)** else [you can skip this section](#If-you-are-new-to-jupyter Notebooks) <br>


#### **If you know some Python, but are new to Jupyter Notebooks, continue with the instructions [here](/learn_jupyter.md)** else [you can skip this section](#if-you-are-a-coder-and-comfortable-with-python) <br>


#### **If you are a coder and comfortable with Python**<br>
If you are an advanced user, feel free to clone this Github repository to your local device. You can install the required libraries with the `requirements.txt` file and visiting the [notebooks folder](notebooks). The documentation in the notebooks should provide all information needed. 

----------------------------------------------

<br>
<br>


## Repository Structure 

```
data-repo-mvp
 ┣ data: Holds raw and processed data used in notebooks. 
 ┃ ┣ extracted_data: Processed or semi-processed data generated from notebooks. 
 ┃ ┗ raw_source_files: Raw files downloaded from sources, for instance PDF files. 
 ┣ misc: Holds miscellaneous files used in this repo, can be ignored.
 ┣ notebooks: Jupyter/Colab notebooks used to extract/scrape/download data. 
 ┣ src: Folder contains different scripts used to extract datasets. These scripts are similar
 ┃       in content to certain notebooks but can be run automatically on predefined schedules. 
 ┣ README.md
 ┗ requirements.txt: File that contains all the Python requirements used in this repository. 
```

## Tools Used
* [Python 3](https://docs.python.org/3/)
* [Jupyter Notebooks](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html)
* Java 8
<br>

## License 
    TBD 

--------------------------------

# Contact Us: 

Have questions? See an issue? Want help? Don't hesitate to contact us!
* datarepo@emersoncollective.com **<span style="color:red">TO DO: make a general email for this product, or use the products team email<s/pan>**
