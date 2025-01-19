"""
Author: Jagadish
Purpose: Web scraping script to extract Olympic medal data from Olympedia.org.

"""

import pandas as pd
import requests
from bs4 import BeautifulSoup

data = []
current_page = 1

while True:
    try:
        # Skip pages 27 and 28
        if current_page in [27, 28]:
            print(f"Skipping page {current_page} (missing data).")
            current_page += 1
            continue

        url = f'https://www.olympedia.org/editions/{current_page}/medal'
        page = requests.get(url, timeout=10)  # Add timeout to prevent hanging requests

        # Check if the page exists
        if page.status_code == 404:
            print(f"Page {current_page} not found (status code: {page.status_code}). Stopping.")
            break

        if page.status_code != 200:
            print(f"Error on page {current_page} (status code: {page.status_code}). Stopping.")
            break

        soup = BeautifulSoup(page.text, 'html.parser')

        # Extract the <h1> tag
        h1_text = soup.find('h1')
        h1_text = h1_text.text.strip() if h1_text else "No Title Found"

        # Find the table on the page
        table = soup.find('table', class_="table")

        # If no table is found, skip to the next page
        if not table:
            print(f"No table found on page {current_page}. Skipping.")
            current_page += 1
            continue

        # Process table rows
        for row in table.find_all('tr')[1:]:  # Skip header row
            cols = row.find_all('td')
            row_data = [col.text.strip() for col in cols]
            row_data.insert(0, h1_text)  # Add the h1 text as the first column
            data.append(row_data)

        print(f"Processed page {current_page} with title: {h1_text}")
        current_page += 1

    except requests.exceptions.RequestException as e:
        print(f"Request error on page {current_page}: {e}. Stopping.")
        break

    except Exception as e:
        print(f"Unexpected error on page {current_page}: {e}. Stopping.")
        break

# Ensure consistent column headers
try:
    if data:
        # Determine the maximum number of columns in the data
        max_columns = max(len(row) for row in data)
        column_headers = ["Page Title"] + [f"Column{i}" for i in range(1, max_columns)]

        # Normalize all rows to have the same length
        normalized_data = [row + [""] * (max_columns - len(row)) for row in data]

        # Create DataFrame
        df = pd.DataFrame(normalized_data, columns=column_headers)

        # Save to CSV
        try:
            df.to_csv('olympics_data.csv', index=False)
            print("Data saved to 'olympics_data.csv'.")
        except IOError as e:
            print(f"Error saving data to CSV: {e}")
    else:
        print("No data scraped.")
except Exception as e:
    print(f"An unexpected error occurred during data processing: {e}")
