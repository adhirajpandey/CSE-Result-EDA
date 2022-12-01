# CSE-Result-EDA
# Description

This is an Exploratory Data Analysis Project to Extract data from University's result portal to Transform, Load, Analyze and Visualize it to gain insights.
Used Python Libraries like Selenium, Beautiful Soup, Pandas to automate the extraction process, parse the html data to make it structured and clean/transform the dataset respectively.
Used sqlite3 to store the curated Database and Tableau to visualize data to gather Insights.


# Requirements

- python3
- pip3
- os
- json
- beautifulsoup4
- pandas
- csv
- sqlite3

# Files and Folders Description

- Raw Results: Contains the raw results of all the students of all branches in the form of html files.

- DB: Contains the final csv files of the students database branchwise.

- scrape.py - This script uses selenium to automate the process of entering roll number and extracting the data from the result portal in html format and stores it in output directory defined by user.
- makedb.py - This script uses beautifulsoup, pandas, csv to parse the saved html result files and store it in structured format in a csv file, takes -b branch argument.

- mergedbs.py - This script uses pandas to merge the csv files of all branches into a single csv file.

- cleandb.py - This script uses pandas to clean the merged csv file and store it in a new csv file.

- results.db - This is the final database file created using sqlite3.

- dashboard.twbx - This is the final dashboard created using Tableau to Visualize the data.

# Miscellaneous

- The data is extracted from the result portal (OneView) of the Dr. A.P.J. Abdul Kalam Technical University, Lucknow.
- The data is of the students of the 2020-2024 batch of the Computer Science and Engineering Department of MIET College.
- The analysis is done on the 2nd Year results of the students.
- The final cleaned data is stored in the results.db file so further it can be used with SQL queries to gain more insights.
- The dashboard.twbx file contains the final dashboard created using Tableau and is hosted on Tableau Public.
Check it out here: https://public.tableau.com/app/profile/adhiraj.pandey3901/viz/CSEResultEDA/Dashboard1




   

