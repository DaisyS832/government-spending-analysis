# Government Spending & Budget Analysis (DMV Focused)

## Project Overview

This project analyzes federal contract spending data across the DMV region, specifically Maryland, Virginia, and Washington, DC. The analysis focuses on identifying spending distribution across states, agencies, contract recipients, and industries using Python, Jupyter Notebook, and large-scale government spending datasets.

The goal of this project was to demonstrate practical data analytics skills including data cleaning, exploratory analysis, automation, visualization, and business-focused insight generation using real federal contract data.

The project combines structured data processing with visual storytelling to highlight patterns in government contract activity throughout the DMV region.

## Business Problem

Federal spending data is extremely large and difficult to analyze without proper cleaning and organization. Government agencies, contractors, and analysts often need to understand where funding is concentrated, which industries receive the highest contract value, and which agencies dominate spending activity.

This project addresses that problem by transforming raw federal contract data into a cleaned, DMV-focused analytical dataset that can be used to identify spending trends and major government contracting activity within the region.

## Objectives

The main objectives of this project were:

- Clean and structure raw federal spending data
- Filter spending records to DMV-focused locations
- Analyze spending distribution across states
- Identify the top awarding agencies
- Identify the largest contract recipients
- Analyze industry concentration
- Generate reusable outputs and visualizations
- Build a professional analytics repository using Python and Jupyter Notebook

## Tools & Technologies

- Python
- Pandas
- Matplotlib
- Jupyter Notebook
- CSV
- Excel
- GitHub

## Dataset

The raw dataset used in this project was derived from federal contract spending data originally sourced from USAspending.gov.

The dataset includes information related to:

- Contract recipients
- Awarding agencies
- Funding agencies
- Award values
- Industry classifications
- Cities and states
- Contract descriptions
- Performance locations

The analysis specifically focuses on records associated with:

- Maryland (MD)
- Virginia (VA)
- Washington, DC

## Data Cleaning Process

The cleaning workflow included:

- Selecting relevant analytical columns
- Filtering records to DMV states only
- Converting date fields into datetime format
- Converting award values into numeric format
- Removing missing values
- Removing invalid or negative award values
- Removing duplicate records
- Creating processed CSV and Excel outputs
- Creating GitHub-friendly sample datasets

## Data Preview

![Data Preview](images/data_preview.png)

The preview above shows the cleaned DMV-focused federal contract dataset after processing and filtering.

## Visualizations

### Federal Contract Spending by DMV State

![Federal Spending by State](government-spending-analysis/images/spending_by_state.png)

This visualization compares total federal contract spending across Maryland, Virginia, and Washington, DC.

### Top Awarding Agencies

![Top Agencies](government-spending-analysis/images/top_agencies.png)

This visualization highlights the agencies responsible for the highest federal contract spending within the DMV dataset.

### Top Contract Recipients

![Top Recipients](government-spending-analysis/images/top_recipients.png)

This chart identifies the organizations and contractors receiving the largest federal contract values.

### Top Industries by Contract Value

![Top Industries](government-spending-analysis/images/top_industries.png)

This visualization shows the industries receiving the highest overall contract funding across the DMV region.

## Key Insights

- Maryland and Virginia represent the largest share of federal contract value within the DMV dataset.
- The Department of Defense dominates federal contract spending activity.
- Large federal contractors such as Lockheed Martin, Maximus Federal Services, Booz Allen Hamilton, Leidos, and Northrop Grumman appear among the highest-funded recipients.
- Engineering, shipbuilding, computer systems design, research and development, and facilities support services represent major industry categories.
- Federal spending activity in the DMV region is heavily concentrated around defense, technology, and research-related sectors.

## Project Structure

```text
government-spending-analysis/
│
├── data/
│   ├── raw/
│   │   └── raw_federal_spending.csv
│   │
│   └── processed/
│       ├── cleaned_data.csv
│       ├── cleaned_data.xlsx
│       ├── cleaned_data_sample.csv
│       └── cleaned_data_sample.xlsx
│
├── images/
│   ├── data_preview.png
│   ├── spending_by_state.png
│   ├── top_agencies.png
│   ├── top_industries.png
│   └── top_recipients.png
│
├── notebooks/
│   └── analysis_notebook.ipynb
│
├── outputs/
│   ├── spending_by_state.csv
│   ├── top_agencies.csv
│   ├── top_industries.csv
│   └── top_recipients.csv
│
├── scripts/
│   ├── data_cleaning.py
│   └── analysis.py
│
├── docs/
│   └── project_notes.md
│
├── README.md
└── .gitignore

## Data Accessibility

The full dataset used in this project is large and may not preview easily within GitHub. To improve accessibility and reviewability, smaller cleaned sample datasets are included inside the data/processed/ folder.

Included sample files:

cleaned_data_sample.csv
cleaned_data_sample.xlsx

These files allow quick review of the cleaned dataset structure without requiring the full dataset to be opened.

## Outputs

The project also includes exported analytical summary files inside the outputs/ folder:

spending_by_state.csv
top_agencies.csv
top_industries.csv
top_recipients.csv

These outputs provide reusable summarized results for additional reporting or visualization.

## Conclusion

This project demonstrates the ability to clean and process large government datasets, automate data preparation workflows, perform exploratory analysis, generate visual insights, and communicate findings clearly using Python and Jupyter Notebook.

The project also demonstrates practical public-sector analytics skills relevant to government contracting, budget analysis, and regional economic analysis within the DMV area.

By combining technical implementation with business-focused interpretation, this project provides a complete example of applied data analytics using real federal spending data.

## Author

Daisy Sharma
