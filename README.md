# The Immigration Data Repository 

## Background 
The Immigration Data Repo is powered by the Emerson Collective. This is a place where we post immigration related datasets that have been collected (typically by us). The data comes mostly from public sources. 

You can use this repository to datasets to use here, but to also...
* download the data
* get a sense of how the data was collected
* learn how to use, and adapt, code to procure and format immigration datasets from the web
* connect and engage with a community of trusted peers to learn from/with
* contribute any code and/or datasets you may wish to the community

Have any questions? Feel free to [get in touch with us!](#contact-us)

<br>

## Getting Started 

### 1. Are you just looking for the data?
 
 See the [Data Inventory](#data-inventory) table. The links in the **See Data** column will connect you to where the extracted data for that specific source is located. 
 * We update select datasets as new data gets released 
 <span style="color:red">**!! TBD - not yet true but hopefully soon!!**</span> 
 * Data outputs may be in the form of a single file or multiple files depending on the source. 

We recommend reviewing the code notebooks used to generate the data to allow for better understanding of how to extract such information and what the data structure will be. 

<br>

### 2. Would you like to review and run the code used to generate data? 

Fantastic ! We have used code notebooks (called Jupyter Notebooks) to write Python code to extract the different datasets. 

#### **If you are new to Python, continue with the instructions below** else [you can skip this section](#If-you-are-new-to-Jupyter Notebooks-continue-with-the instructions below) <br>

So you are new to Python. Welcome! We would love to help you learn a new skill. 

**NOTE: We need to select a resource for remedial Python, and set a benchmark of how much of the course they would have completed. This will help us better understand the level at which we write the language in the notebooks. Below is filler text until we do this**

We highly recommend taking some time to go to [Placeholder Python Learning Place]() and completing the first 2 chapters to understand the basics Python syntax. This should take no more than a few hours of your time.
 
 
Once you have completed this, you can come back here to resume your learning. You will find examples relevant to immigration space that you can run, or even modify and adapt to a different dataset!


#### **If you are new to Jupyter Notebooks, continue with the instructions below** else (you can skip this section)[#if-you-are-a-coder-and-comfortable-with-python] <br>
This code can be run in a number of different ways. For those who are new(-ish) to Python, Jupyter Notebooks are containers that hold code, along with snapshots of outputs, and annotated text, allowing for readability and sharing.

We have created a custom coding environment where you can run these notebooks. This will eliminate the need to manage a Python environment on your local computer. You can begin by visiting our [JupyterHub](TBD). Login with the username and password we have provided. 
<br>
<img src="./misc/images/jupyterhub_signin.png" width="360" height="360">
<br>

Once you have logged in an environment will be started that contains the code notebooks we have created. It may take a couple of minutes for the environment to start up. 
<br>
<img src="./misc/images/jupyterhub_startup.png" width="1000" >
<br>
<br>
Eventually you will be presented with the following screen. 
<br>
<br>
<img src="./misc/images/jupyterhub_enviro.png" width="1000">
<br>
There will be 2 folders, `data-repo` and `lost+found`, you can ignore the `lost+found` folder, but the `data-repo` folder contains the notebooks, data and code we are interested in. Inside `data-repo` there is a folder called `notebooks` please open up this folder. 
     
Hooray ! You've made it and can now start using code to work with immigration data. All code is shared in Jupyter notebooks using the Python programming language. A notebook is a collection of "cells" or areas that you can use to execute code. Each cell is a single block of code, or other information (such as headings, text information, etc.). 


 The various notebooks present in these repo provide a wide variety of functionality for:
    * Downloading PDF files
    * Extracting data from embedded Tableau dashboards on a website and
    * Parsing structured data from PDFs
    * Pulling tables directly from Websites
    * Processing data out of many individual excel files 
    * and more ... 


 To run a cell you can just click the small play button to the far left of any cell.
<br>
<img src="./misc/images/run_a_cell.png" width="330" height="200">
<br>

You can either click each play button or use the keyboard shortcut of SHIFT + ENTER to execute them as well.  We suggest running through notebooks of interest cell by cell. Its ok if you don't understand all of it but at least review the steps that are occurring. Also reference the [Notebooks Readme file](./Notebooks/README.md) and look at the **output data files**. In addition we have saved interim raw files in the [./Data/raw_source_files/](./Data/raw_source_files/) directory. 

We are excited for you to be able to work with these notebooks, see how the concepts and strategies within could be applied to your work more broadly. We suggest starting with those notebooks that are most relevant to you first. 

If you run into any issues or problems please don't hesitate to [let us know](#contactus).



<br>

#### **If you are a coder and comfortable with Python**<br>
Then we suggest just cloning this repository, installing required libraries with the `requirements.txt` file and visiting the [notebooks folder](notebooks). The documentation in the notebooks should provide all information needed. 

----------------------------------------------

<br>
<br>

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
* Python 3
* Google [Colab Notebooks](https://colab.research.google.com/notebooks/intro.ipynb) / [Jupyter Notebooks](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html)
* Java 8
<br>

## License 
    TBD 

--------------------------------

# Contact Us: 

Have questions? See an issue? Want help? Don't hesitate to contact us!
* datarepo@emersoncollective.com **<span style="color:red">TO DO: make a general email for this product, or use the products team email<s/pan>**
