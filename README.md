# The Immigration Data Repository 

## Background 
The Immigration Data Hub (the Data Repo) is ................
* Share code to scrape specific sample of datasets from
* Provide those data samples from
* Highlight how code can be applied to other datasets to allow subject matter experts to obtain the data they need to do their work with
* One can access the downloaded files directly by seeing 


## Getting Started 

### 1. Are you just looking for the data?
 
 See the [Data Inventory](#data-inventory) table. The links in the **See Data** column will connect you to where the extracted data for that specific source is located. 
 * We update the data every 
 <span style="color:red">**!! TBD-TODO !!**</span> 
 * Data outputs may be in the form of a single file or multiple files depending on the source. 

 We recommend reviewing the code notebooks used to generate the data to allow for better understanding of how to extract such information and what the data structure will be. 

### 2. Would you like to review and run the code used to generate data? 

Fantastic ! We have used code notebooks (called Jupyter Notebooks) to write Python code to extract the different datasets. 

**If you are new to Python and Jupyter Notebooks**<br>
This code can be run in a number of different ways but we recommend utilizing google colab notebooks initially to review and run this code. 

* Step 1: 
    * Download this google [folder](https://drive.google.com/drive/folders/1lw3NcE8jEQxgZISVknKUSpJKcFc-6Ruq?usp=sharing) ![Download data-repo-mvp as zip](./misc/images/gdrive_download_repo.png)

  

**If you are a coder and comfortable with python**<br>
Then we suggest just cloning this repository and visiting the [notebooks folder](notebooks) 

----------------------------------------------

## Tools Used
* Python 3
* Google [Colab Notebooks](https://colab.research.google.com/notebooks/intro.ipynb) / [Jupyter Notebooks](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html)

## Repository Structure 
```
data-repo-mvp
 ┣ data: Holds raw and processed data used in notebooks. 
 ┃ ┣ extracted_data: Processed or semi-processed data generated from notebooks. 
 ┃ ┗ raw_source_files: Raw files downloaded from sources, for instance PDF files. 
 ┣ notebooks: Jupyter/Colab notebooks used to extract/scrape/download data. 
 ┣ src: Folder to hold generic code used in the notebooks for specific data tasks. 
 ┗ README.md
## Repository Structure 
```


## Data Inventory 

| Dataset Name      | Source | Updated Regularly? | Original URL      | See Data | Status| 
| ----------- | ----------- | --- | ----------- | ----------- | -- | 
| Encounters      | CBP       | Yes | [source](https://www.cbp.gov/newsroom/stats/southwest-land-border-encounters)      | Title       | (status) |
| Visa Issuances   | USCIS        | Yes | [source](https://travel.state.gov/content/travel/en/legal/visa-law0/visa-statistics.html)      | Title       | (status) |
| (name)   | US Census        | No? | Header      | Title       | (status) |
| (name)   | US Census        | No? | Header      | Title       | (status) |




**Running






## License 
    TBD 

--------------------------------

**Contact**: mdowd@emersoncollective.com, ada@emersoncollective.com, dat@emersoncollective.com

### My Multi Word Header
