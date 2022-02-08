<!--THINGS TO ADD
* Recommend hte user to make a folder to work with inthere, port over copies to the folder
* “Any changes you made will not be changed unless you make a copy


-->

# The Immigration Data Repository 

*...powered by the Emerson Collective!*

## Background 
The Immigration Data Repository is a place where you can find immigration-related datasets that we have sourced, assembled, and converted into easy-to-use formats. 

We have designed the respository to allow you to explore our work in various ways, including...
* downloading the datasets that are presented in easy-to-use formats
* understanding how the data was collected
* learning how to use and adapt our code to procure and wrangle similar datasets

The Data Repository can be accessed and viewed in two ways.:
* [JupyterHub View](http://data-repo.emersoncollective.tech/) - recommended for beginning and intermediate users
* [Github View](https://github.com/emersoncollective/data-repo-mvp) - recommended for advanced users (*please request access from EC*)

Don't know which to use? Continue reading to learn more about which way of accessing the data is right for you!

<br>

**Have any questions? Or ideas for additional datasets that could be useful?** Feel free to [get in touch with us!](#contact-us)

**Do you want to connect and engage with a community of trusted peers to learn from/with?** Feel free to [join our Slack Channel **TBD**!]()

**Do you have any code or datasets you want to share with this community?** Feel free to [let us know!]((#contact-us))

<br>

## Getting Started 

### 1. Are you just looking for the data?
 
See the [Data Inventory](#data-inventory) table below. The links in the **See Data** column will connect you to where the extracted data for that specific source is located. 
 * We update select datasets as new data gets released
 * Data outputs may be in the form of a single file or multiple files depending on the source. 

**Data Inventory**

|   | Dataset Name                                                                      | Source                          | Original URL                                                                              | See Data                                          | See Code                                                    | Updated Regularly? |
| - | --------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------- | ----------------------------------------------------------- | ------------------ |
| 1 | CBP Southwest Land Border Encounters                                              | CBP                             | [source](https://www.cbp.gov/newsroom/stats/southwest-land-border-encounters)             | [dataset ](data/extracted_data/cbp-tableau)       | [code](Notebooks/CBP-Encounters.ipynb)                      | Yes                |
| 2 | U.S. Border Patrol Nationwide Apprehensions by Citizenship and Sector FY2007-2020 | CBP                             | [source ](https://www.cbp.gov/sites/default/files/assets/documents/2021-Aug/USBORD~3.PDF) | [dataset ](data/extracted_data/cbp-apprehensions) | [code](Notebooks/CBP-Apprehensions.ipynb)                   | No                 |
| 3 | State Department Monthly Visa Issuances                                           | US State Department             | [source](https://travel.state.gov/content/travel/en/legal/visa-law0/visa-statistics.html) | [dataset ](data/extracted_data/state-dept)        | [code](Notebooks/STATE-DEPT-Monthly-Visa-Stats.ipynb)       | *TBD*                |
| 4 | EOIR Asylum Decision Rates by Nationality                                         | US Department of Justice / EOIR | [source](https://www.justice.gov/eoir/page/file/1107366/download)                         | [dataset ](data/extracted_data/doj)               | [code](Notebooks/DOJ-Asylum-Decisions-by-Nationality.ipynb) | *TODO*               |
| 5 | USCIS Congressional Semi-Monthly Report (CFR/RFR)                                 | US State Department             | [source](https://travel.state.gov/content/travel/en/legal/visa-law0/visa-statistics.html) | *TBD*                                               | [code](Notebooks/USCIS-Credible-Fear-Spreadsheets.ipynb)    | *TBD*                |
| 6 | US Census Miscellaneous                                                           | US Census                       | [source](https://data.census.gov/cedsci/)                                                 | NA                                                | [code](Notebooks/Census-Data.ipynb)                         | No                 |
| … | More to come                                                                      |                                 |                                                                                           |                                                   |                                                             |                    |

<br>

We recommend reviewing the code notebooks used to generate the data to allow for better understanding of how to extract such information and what the data structure will be. 

<br>

### 2. Would you like to review and run the code used to generate data? 

Fantastic! We have used code notebooks (Jupyter Notebooks) to write Python code to extract the different datasets. The Notebooks are annotated to explain the methodology in a stepwise manner. We host the Notebooks on an interactive evironment (JupyterHub) so that you can run the code yourself if you like! The JupyterHub environment has everything you need to run the code -- there is no need to install Python or to maintain a Python environment on your computer. You can also write and run your own code on your JupyterHub.







**If you are new to the Immigration Data Repository...** you will need to [sign-up for an account](http://34.133.178.202/hub/signup). This will create your own instance of the Data Repository, complete with copies of the code. Feel free to work within your account -- any code you run or edit will remain private, and any changes made to the notebooks provided by the Emerson Collective will be reflected on your account.


#### **If you are new to Python, check out some resources we have compiled [here](./learn_python/).** 
We recommend completing a set of basic Python coursework to help you understand what the code on this repository is doing at a high-level.


#### **If you know some Python, but are new to Jupyter Notebooks, check out some resources we compiled [here](./learn_jupyter/)** 
These resources will help you understand the basic functionality of Jupyter Notebooks, such as how to run code on a notebook, and how to make a notebook of your own.


#### **If you are a coder and are comfortable with Python**<br>
If you are an advanced user, feel free to clone the Github repository to your local device. At present, the Github view is private, however feel free to [get in touch with us!](#contact-us) to request access. You can install the required libraries with the `requirements.txt` file and visiting the [notebooks folder](./Notebooks). The documentation in the notebooks should provide all information needed. 

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
<br>

## License 
    TBD 

## How to Cite Us 
    TBD 

--------------------------------

# Contact Us: 

Have questions? See an issue? Want help? Don't hesitate to contact us!
* datarepo@emersoncollective.com
* tech_product@emersoncollective.com
