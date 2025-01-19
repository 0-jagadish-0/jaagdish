# Author: Jagadish
# Description: This script scrapes a Wikipedia page for a list of countries and their capitals in native languages,
# extracts data from the tables using Beautiful Soup, organizes it into a pandas DataFrame, and saves it to a CSV file.

import requests  # Library to send HTTP requests and get the webpage content
from bs4 import BeautifulSoup  # Library for parsing HTML content
import pandas as pd  # Library for data manipulation and storage

# URL of the Wikipedia page to scrape
target_url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_and_their_capitals_in_native_languages"

# Send a GET request to the URL and store the response
response = requests.get(target_url)

# Parse the page content with Beautiful Soup
soup = BeautifulSoup(response.text, 'html.parser')

# Initialize an empty list to store data from all tables
all_data = []

# Find all tables with the class "wikitable"
tables = soup.find_all('table', class_="wikitable")

# Iterate over each table
for table in tables:
    # Extract the header row from the table and clean the column names
    header = [th.text.strip() for th in table.find_all('th')]

    # Initialize a list to store rows of the table
    rows = []

    # Iterate over each row in the table
    for row in table.find_all('tr'):
        # Find all cells (both header and data) in the row and extract their text
        cols = row.find_all(['th', 'td'])
        rows.append([col.text.strip() for col in cols])

    # If rows are found, create a pandas DataFrame and add it to the data list
    if rows:
        all_data.append(pd.DataFrame(rows, columns=header))

# If data was successfully extracted from tables
if all_data:
    # Concatenate all DataFrames into a single DataFrame
    final_df = pd.concat(all_data)

    # Print the final DataFrame
    print(final_df)

    # Save the DataFrame to a CSV file
    final_df.to_csv("caps.csv", index=False)  # Ensure the index is not included in the CSV file

