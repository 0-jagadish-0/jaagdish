"""
Script to Scrape Country Population Data from Wikipedia
Author: Jagadish

This script scrapes population data for countries and dependencies from the Wikipedia page:
https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population

The scraped data includes headers such as rank, country name, population, and more. The data is stored 
in a Pandas DataFrame for further analysis or export.
"""

import pandas as pd  # Library for creating and manipulating data in tabular format
import requests  # Library for sending HTTP requests to fetch webpage content
from bs4 import BeautifulSoup  # Library for parsing HTML content and extracting data


url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"  # Wikipedia URL containing the data

page = requests.get(url)  # Send an HTTP GET request to fetch the webpage content

soup = BeautifulSoup(page.text, 'html.parser')  # Parse the HTML content using BeautifulSoup


table = soup.find('table', class_='wikitable')  # Find the table with class 'wikitable' that contains the data

header = [th.text.strip() for th in table.find_all('th')]  # Extract table headers and strip unnecessary whitespace


rows = []  # Initialize an empty list to store the rows of data

for row in table.find_all('tr')[1:]:  # Loop through all table rows, skipping the header row
    cols = row.find_all(['tr', 'td'])  # Extract data from each column in the row
    rows.append([col.text.strip() for col in cols])  # Strip whitespace and append row data to the list


df = pd.DataFrame(rows, columns=header)  # Convert the list of rows into a Pandas DataFrame using extracted headers


df.to_csv("countries.csv")
