import pandas as pd
import csv
from tabulate import tabulate
data = pd.read_csv("1970-2021_DISASTERS.csv")

#DATA CLEANING

#keeping only the columns we want
data = data[['Year', 'Country', 'Region', 'Continent', 'Location',
             'Disaster Group', 'Disaster Subgroup', 'Disaster Type', 'Disaster Subtype',
             'Event Name', 'Start Year', 'Start Month', 'End Year', 'End Month',
             'Total Deaths', 'No Injured', 'No Affected', 'No Homeless',
             'Total Affected', "Reconstruction Costs ('000 US$)", "Insured Damages ('000 US$)",
             "Total Damages ('000 US$)"]]

#renaming some columns
data = data.rename(columns={"Reconstruction Costs ('000 US$)": "Reconstruction Costs",
                   "Insured Damages ('000 US$)": "Insured Damages", "Total Damages ('000 US$)":
                   "Total Damages"})

#fixing month columns to show month name
data['Start Month'].fillna("N/A", inplace=True)
data['End Month'].fillna("N/A", inplace=True)
months = {"N/A": "N/A", 1.0: 'Jan', 2.0: 'Feb', 3.0: 'Mar', 4.0: 'Apr', 5.0: 'May',
          6.0: 'Jun', 7.0: 'Jul', 8.0: 'Aug', 9.0: 'Sep', 10.0: 'Oct',
          11.0: 'Nov', 12.0: 'Dec'}
data['Start Month'] = data['Start Month'].apply(lambda x: months[x])
data['End Month'] = data['End Month'].apply(lambda x: months[x])

#fixing missing values in cost columns
data['Reconstruction Costs'].fillna("0", inplace=True)
data['Insured Damages'].fillna("0", inplace=True)
data['Total Damages'].fillna("0", inplace=True)
data['No Injured'].fillna("0", inplace=True)
data['No Affected'].fillna("0", inplace=True)
data['No Homeless'].fillna("0", inplace=True)
data['Total Affected'].fillna("0", inplace=True)
data['Total Deaths'].fillna("0", inplace=True)

#fixing united states value
data["Country"] = data["Country"].replace("United States of America (the)",
                                          "United States of America")
data["Country"] = data["Country"].replace("Philippines (the)", "Philippines")

#now i will import dataset into a new csv file
data.to_csv("DISASTERS_cleaned.csv", sep=',', encoding='utf-8')
data1 = pd.read_csv("DISASTERS_cleaned.csv")
data1 = data1.rename(columns={'Unnamed: 0': "id"})
data1.to_csv("DISASTERS_cleaned.csv", sep=',', encoding='utf-8', index=False)

for i in data1:
    print(i)