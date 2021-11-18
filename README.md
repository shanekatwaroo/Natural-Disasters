# Natural-Disasters

## Overview
- This project features an analysis of natural disasters in the past 50 years (1970-2020). The programs used for this project include python for data cleaning through the use of the pandas module, MySQL to answer some KPI's about the data, and finally Tableau to visually represent the KPI findings. 
## Branches:
**main.py:** used to clean data and create a new csv with cleaned data\
**analyze.py:** used to connect to SQL database and answer KPI's\
**1970-2020_disasters.csv:** main dataset(downloaded from kaggle)\
**disasters_cleaned.csv:** cleaned dataset used for project\
**results.md:** final results with tableau visualizations\

## Sources
- This project utilized a dataset that I found on kaggle. Here is the link to the dataset: 
https://www.kaggle.com/brsdincer/all-natural-disasters-19002021-eosdis
(Description: As we know, the global climate disaster makes its impact on us more felt day by day. Understanding the parameters created by the climate crisis will be helpful in deciding the measures we will take against it.
In this dataset, you will see the natural disasters of all countries.)

- The dataset contains many columns, however, whilst cleaning my data I only decided to keep a few of these columns. Below are the columns I utilized:

  **id, Year, Country, Region, Continent, Location, Disaster Group, Disaster Subgroup, Disaster Type, Disaster Subtype, Event Name, Start Year, Start Month, End Year, End Month, Total Deaths, No Injured, No Affected, No Homeless, Total Affected, Reconstruction Costs, Insured Damages, Total Damages**
  
## Project Steps
- Using the csv file containing the disasters from 1970-2020, I imported the csv into python and did some data cleaning. The main.py file contains the code in which selects certain columns to include into a new csv file, entitles "disasters_cleaned.csv". It is this file that I used to answer my KPI's.
- The next py file, entitles "analyze.py" is used to connect to a mySQL database. I import all the data from this new csv file into this database to answer the KPI's.
- Finally, I import the csv file into Tableau and created some visuals. Heres the link to the Tableau workbook: https://public.tableau.com/views/NaturalDisasters_16370419786110/Sheet1?:language=en-US&:display_count=n&:origin=viz_share_link
