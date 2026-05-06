# Project Notes

## Project Summary

This project analyzes federal contract spending in the DMV region, focusing on Maryland, Virginia, and Washington, DC. The goal is to identify how federal contract value is distributed across states, agencies, recipients, and industries.

## Dataset

The raw dataset comes from federal award data originally sourced from USAspending.gov. The raw file was preserved in the `data/raw/` folder, while a cleaned DMV-focused version was created in the `data/processed/` folder.

## Cleaning Process

The cleaning process included selecting relevant columns, filtering records to DMV states, converting date fields, converting award values into numeric format, removing missing values, removing non-positive award values, and dropping duplicate records.

## Analysis Performed

The analysis focused on four major areas:

- Federal contract spending by DMV state
- Top awarding agencies by contract value
- Top contract recipients by award value
- Top industries by contract value

## Key Findings

Maryland and Virginia represent the largest share of contract value in the cleaned DMV dataset, while Washington, DC shows a smaller overall total. The Department of Defense is the dominant awarding agency, and major government contractors such as Lockheed Martin, Maximus Federal Services, Booz Allen Hamilton, Leidos, and Northrop Grumman appear among the top recipients.

The industry analysis shows strong concentration in ship building, computer systems design, engineering services, research and development, and facilities support services.

## Business Relevance

This project is relevant to public-sector analytics, government contracting, budget analysis, and regional economic analysis. It demonstrates how federal spending data can be cleaned, filtered, summarized, and visualized to support decision-making in the DMV region.

## Tools Used

- Python
- Pandas
- Matplotlib
- Jupyter Notebook
- CSV and Excel files