# Author: Jagadish
# Description: This script scrapes a cricket statistics website to extract a list of cricket players alphabetically,
# processes the data into a pandas DataFrame, and saves it into a CSV file.

import requests  # Library to send HTTP requests and get the webpage content
import pandas as pd  # Library for data manipulation and storage
from bs4 import BeautifulSoup  # Library for parsing HTML content

# Initialize an empty list to store all player data
all_rows = []

# Iterate over each letter in the alphabet to fetch players grouped by their starting letter
for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    # URL of the cricket statistics page for the current letter
    url = f'https://www.howstat.com/Cricket/Statistics/Players/PlayerList.asp?Country=ALL&Group={letter}'
    
    # Send a GET request to the URL and store the response
    page = requests.get(url)
    
    # Parse the page content with Beautiful Soup
    soup = BeautifulSoup(page.text, 'html.parser')

    # Find the table containing player data using its class name
    table = soup.find('table', class_='TableLined') 
    if table:  # Proceed only if the table is found
        # Iterate over each row in the table
        for row in table.find_all('tr'): 
            # Find all cells in the row and extract their text
            cols = row.find_all('td') 
            cols_text = [col.text.strip() for col in cols]  # Clean up whitespace from cell text
            if cols_text:  # Add the row to all_rows only if it contains data
                all_rows.append(cols_text)

# Create a pandas DataFrame from the collected data
# Note: Since the table headers are not explicitly defined, the DataFrame will not have column names
# You can add column names later if required

df = pd.DataFrame(all_rows)

# Save the DataFrame to a CSV file
# The file is named "cricket_player.csv" and will be created in the current working directory
df.to_csv("cricket_player.csv", index=False)
