
"""
Script for Web Scraping Quotes
Author: Jagadish

This script scrapes quotes, their authors, and tags from the website 'https://quotes.toscrape.com'. 
The data is saved into a CSV file named 'quotes.csv'.
Libraries used:
- pandas: For data manipulation and saving to a CSV file
- requests: For making HTTP requests to fetch web pages
- BeautifulSoup: For parsing and extracting data from HTML
"""


import pandas as pd  # Library to create and manipulate data in tabular format
import requests  # Library to make HTTP requests to fetch webpage content
from bs4 import BeautifulSoup  # Library for parsing and extracting data from HTML

current_page = 1  # Start scraping from the first page
data = []  # Initialize an empty list to store the scraped data


while True:  # Infinite loop to iterate through pages until no quotes are found
    url = f"https://quotes.toscrape.com/page/{current_page}/"  # Construct URL dynamically for each page
    page = requests.get(url)  # Send an HTTP GET request to fetch the page content
    soup = BeautifulSoup(page.text, 'html.parser')  # Parse the HTML content with BeautifulSoup

    all_quotes = soup.find_all("div", class_="quote")  # Find all quote elements on the page
    if not all_quotes:  # If no quotes are found, break the loop and stop scraping
        break

    for quote in all_quotes:  # Loop through all quotes on the current page
        item = {}  # Initialize an empty dictionary to store quote details
        item['author'] = quote.find('small', class_="author").text  # Extract the author's name
        item['quote'] = quote.find('span', class_='text').text  # Extract the quote text
        item['tags'] = [tag.text for tag in quote.find_all("a", class_='tag')]  # Extract all tags for the quote
        data.append(item)  # Append the dictionary to the data list

    current_page += 1  # Move to the next page by incrementing the page number


# Create a Pandas DataFrame from the scraped data
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file named 'quotes.csv'
df.to_csv('quotes.csv', index=False)

# Print a confirmation message after saving the data
print("Data saved to 'quotes.csv'.")



    
