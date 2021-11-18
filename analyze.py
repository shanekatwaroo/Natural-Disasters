import mysql.connector
import csv
from tabulate import tabulate

#now we connect to sql database to answer some kpi's
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="password",
    database="disaster"
)
mycursor = db.cursor(buffered=True)

mycursor.execute('DROP TABLE IF EXISTS main')
sql = """CREATE TABLE main (
            id INT NOT NULL primary key,
            Year INT(10),
            Country varchar(100),
            Region varchar(100),
            Continent varchar(50),
            Location text,
            Disaster_Group varchar(100),
            Disaster_Subgroup varchar(100),
            Disaster_Type varchar(100),
            Disaster_Subtype varchar(100),
            Event_Name varchar(100),
            Start_Year INT(10),
            Start_Month varchar(50),
            End_Year INT(10),
            End_Month varchar(50),
            Total_Deaths bigint,
            No_Injured bigint,
            No_Affected bigint,
            No_Homeless bigint,
            Total_Affected bigint,
            Reconstruction_Costs bigint,
            Insured_Damages bigint,
            Total_Damages bigint);"""  # adds columns to table
mycursor.execute(sql)

# now we input values into these columns
data = open('DISASTERS_cleaned.csv')
csv = csv.reader(data, delimiter=',')
all_values = []
next(csv)
for row in csv:
    value = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],
             row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17],
             row[18], row[19], row[20], row[21], row[22])
    all_values.append(value)

sqlinsert = "INSERT INTO main VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s," \
            "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
mycursor.executemany(sqlinsert, all_values)
db.commit()

#KPI 1: Which countries(top 5)has had the largest amount of natural disasters?
query1 = """SELECT Country, COUNT(id)
            FROM main
            GROUP BY Country
            ORDER BY COUNT(id) DESC LIMIT 5;"""
mycursor.execute(query1)
#result = mycursor.fetchall()
#print(tabulate(result,headers=("Country","Count"),tablefmt="pretty"))

#KPI 2: What is the most common type of natural disaster?
query2 = """SELECT Disaster_Type, COUNT(Disaster_Type)
            FROM main
            GROUP BY Disaster_Type
            ORDER BY COUNT(Disaster_Type) DESC LIMIT 5;"""
mycursor.execute(query2)
#result = mycursor.fetchall()
#print(tabulate(result, headers=("Disaster Type", "Count"), tablefmt="pretty"))

#KPI 3: Have the amount of natural disasters increased over the years?
query3 = """SELECT Year, COUNT(id)
            FROM main
            WHERE Year > 1990
            GROUP BY Year
            ORDER BY COUNT(id) DESC"""
mycursor.execute(query3)
#result = mycursor.fetchall()
#print(tabulate(result, headers=("Year", "Count"), tablefmt="pretty"))

#KPI 4: Which type of natural disaster is considered the deadliest?
query4 = """SELECT Disaster_Type, Total_Deaths
            FROM main
            ORDER BY Total_Deaths DESC LIMIT 1;"""
mycursor.execute(query4)
#result = mycursor.fetchall()
#print(tabulate(result, headers=("Type", "# of Deaths"), tablefmt="pretty"))

#KPI 5: What type of natural disaster is most common based on country?
query5 = """SELECT Country, Disaster_type, COUNT(*) as Total
            FROM main a
            GROUP BY Country, Disaster_Type
            HAVING COUNT(*) = (
                    SELECT COUNT(*)
                    FROM main
                    WHERE Country = a.Country
                    GROUP BY Country, Disaster_Type
                    ORDER BY COUNT(*) DESC LIMIT 1
                  )
            ORDER BY Total DESC LIMIT 5"""
mycursor.execute(query5)
result = mycursor.fetchall()
print(tabulate(result, headers=("Country", "Type","Total #"), tablefmt="pretty"))

#KPI 6: Which region of the world is most affected by natural disasters?
query6 = """SELECT Region, COUNT(id)
            FROM main
            GROUP BY Region
            ORDER BY COUNT(id) DESC LIMIT 5;"""
mycursor.execute(query6)
#result = mycursor.fetchall()
#print(tabulate(result, headers=("Region", "# of Disasters"), tablefmt="pretty"))

#KPI 7: What type of natural disaster costed the most in terms of damages?
query7 = """SELECT Disaster_Type, MAX(Total_Damages)
            FROM main
            GROUP BY Disaster_Type
            ORDER BY MAX(Total_Damages) DESC LIMIT 5;"""
mycursor.execute(query7)
#result = mycursor.fetchall()
#print(tabulate(result, headers=("Disaster Type", "Total Cost"), tablefmt="pretty"))