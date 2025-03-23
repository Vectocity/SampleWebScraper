# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 21:25:41 2025

@author: victo
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

# Sample URL, store as page, parse using Beautiful Soup html function
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')

'''Sample commands to verify that the Beautiful Soup has been created, correct table selected
print(soup)
soup.find_all('table')[1]
soup.find_all('table', class_ = 'wikitable sortable')[1]
'''

# Selecting which table to scrape
table = soup.find_all('table')[0]

''' Sample commands to verify that the correct table has been selected
print(table)
soup.find_all('th')
'''

# world_titles: all Headers
world_titles = table.find_all('th')

# strip headers
world_table_titles = [title.text.strip() for title in world_titles]

''' Sample commands to verify that headers have been parsed correctly
print(world_table_titles)
'''

# Creating a pandas dataframe, columns set as headers
df = pd.DataFrame(columns = world_table_titles)

''' Sample commands to verify dataframe creation and input
df
'''

# 'tr' is the values tag in this specific webpage
column_data = table.find_all('tr')

# iterate through rows, assign to pandas dataframe
for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data
''' Sample commands to verify dataframe input
df
'''

# Exporting Pandas Dataframe to CSV
# Since this dataframe starts at index 0, 'index = False' removes the first column
df.to_csv(r'D:\A Projects\Test Outputs\Learn Python.csv', index = False)