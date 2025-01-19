# 📊 Data Analyst Portfolio

Welcome to my data analyst portfolio! This repository showcases my skills, techniques, and projects in data analysis, visualization, and storytelling. Each project reflects my approach to solving real-world problems using data-driven insights.

---

## 🧑‍💻 About Me

I am a data analyst passionate about uncovering meaningful insights from data and driving informed decision-making. With expertise in data cleaning, analysis, and visualization, I strive to turn complex datasets into actionable stories.

**Key Skills:**
- Programming: Python (Pandas, NumPy, Matplotlib, Seaborn, Beautifulsoup, Requests)
- Databases: SQL (MySQL, Oracle)
- Visualization:  Power BI, Excel
- Analysis: Exploratory Data Analysis (EDA), Statistical Analysis, Predictive Modeling

---

## 🌟 Featured Projects

<details>
  <summary>** Web Scraping Projects **</summary>

  ### **1. Web Scraping Quotes**
  - **Description:** This script scrapes quotes, their authors, and tags from the website 'https://quotes.toscrape.com'. 
      The data is saved into a CSV file named 'quotes.csv'. This is my first attempt at web scraping.
  - **Tools Used:** Python (Pandas, Requests, Beautifulsoup)
  - **Key Insights:** 
    - The script demonstrates how to scrape structured data from a website (https://quotes.toscrape.com).
    - Extracts quotes, their respective authors, and associated tags from multiple pages.
    - The collected data is stored in a CSV file (quotes.csv) for further analysis or usage.
  - **Limitations and Areas for Improvement:**
    - Static Website: Works well for static websites like quotes.toscrape.com, but might need adjustments for dynamic or JavaScript-rendered pages.
    - Error and Timeout Handling: Lacks explicit handling for potential errors like network issues or server timeouts.
  - [Explore Project](https://github.com/0-jagadish-0/jagadish/blob/8e3ba3d19bd8e27d7bd870e3be6025d051d68d11/webscarping%20quotes/quotes.py)

  ---

  ### **2. Web Scraping countries_population**
  - **Description:** This project involves web scraping country population data from the Wikipedia page:
      https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population.
      The script extracts tabular data, including the rank, country or dependency name, population, and other relevant details.
      It stores the data in a structured format using Pandas, enabling further analysis or export to a file format like CSV.
  - **Tools Used:** Python (Pandas, Requests, Beautifulsoup)
  - **Key Techniques Demonstrated:** 
    - Dynamic Header Extraction: The script dynamically extracts headers to adapt to changes in the table's structure on the webpage.
    - Handling HTML Tables: Iterates through rows and columns to capture clean, usable data.
    - Data Formatting: Strips extra whitespace for a polished and consistent dataset.
  - **Conclusion:**
    - This project highlights the basics of web scraping, dynamic data extraction, and data structuring using Python.
     The output can be applied to various analytical tasks or saved for future reference. It provides a robust framework for extracting structured data from 
     similar tables on other webpages.
  - [Explore Project](https://github.com/0-jagadish-0/jagadish/blob/18447c00ff8e87986042c93f6cdfb1fdf19b3937/web%20scarping%20countries_population/country.py)

  ---

  ### **3. Web Scraping countries_capitals**
  - **Description:** This project demonstrates how to scrape tabular data from a Wikipedia page and process it into a structured format using Python.
     The data collected includes a list of countries and their capitals in native languages, which is saved in a CSV file for further analysis or sharing.
  - **Tools Used:** Python (Pandas, Requests, Beautifulsoup)
  - **Challenges Solved:** 
    - Extracting multi-table data from HTML.
    - Cleaning and structuring unformatted web data into a readable format.
    - Managing dynamic or inconsistent HTML structures.
  - **Potential Applications:**
    - Automating data collection from public web pages.
    - Creating datasets for research or data analysis projects.
    - Serving as a foundational skill for larger web scraping projects.
  - [Explore Project](https://github.com/0-jagadish-0/jagadish/blob/4ca8198cf1ec988c22674a3e3b460f49e7c2c94d/web%20scarping%20countries_capitals/captials.py)

  ---

  ### **4. Web Scraping cricketers_data**
  - **Description:** This project involves creating a web scraping script to extract a comprehensive list of cricket players from a statistics website, categorized alphabetically.
     The scraped data is processed and stored in a structured format using pandas and saved as a CSV file. This project showcases proficiency in web scraping, data parsing, and storage using Python.
  - **Tools Used:** Python (Pandas, Requests, Beautifulsoup)
  - **Key Features:** 
    - Dynamic URL Handling: Iterates through URLs for all alphabetical categories (A-Z).
    - Data Extraction: Scrapes player names and related details from the target website.
    - HTML Parsing: Utilizes Beautiful Soup to identify and extract data from specific table structures.
    - Data Storage: Converts extracted data into a pandas DataFrame and saves it as a CSV file
  - **Skills Demonstrated:**
    - Web scraping using Beautiful Soup.
    - Efficient data handling and storage using pandas.
    - Automating tasks with Python.
    - Working with HTML and identifying specific elements (e.g., tables).
  - [Explore Project](https://github.com/0-jagadish-0/jagadish/blob/905868aaab5e36aa4a3df844466a83b85febb0df/web%20scarping%20cricket_players_data/circket_players.py)

  ---

  ### **5. Web Scraping olympics_data**
  - **Description:** his project is a Python-based web scraping script designed to extract Olympic medal data from the Olympedia website.
     The script automates the process of gathering structured information from multiple pages and organizes the data into a well-formatted CSV file.
    A key highlight of this project is the inclusion of robust error handling for the first time, making the scraping process more reliable and efficient.
  - **Tools Used:** Python (Pandas, Requests, Beautifulsoup)
  - **Key Features:** 
    - Dynamic Page Navigation: Automatically iterates through multiple pages to scrape data.
    - Error Handling: Implemented error handling for the first time, enabling the script to gracefully handle:
       Missing pages (e.g., skips pages 27 and 28).
       HTTP errors like 404 (Not Found) and other non-200 responses.
       Network-related exceptions (e.g., timeouts).
    - Data Normalization: Ensures consistent column structure across all scraped data.
    - CSV Export: Saves the cleaned and structured data into a CSV file for analysis and sharing.
  - **Challenges Solved:**
    - Successfully addressed missing data pages.
    - Implemented error handling to manage HTTP and network-related issues.
    - Dynamically adjusted column structures for inconsistent table rows.
  - [Explore Project](https://github.com/0-jagadish-0/jagadish/blob/7bb2883fd437df71236f0bdeb8a088f41d91f552/web%20scarping%20oplympics%20data/main.py)

</details>

---

## 📂 Repository Structure

```plaintext
📁 data-analyst-portfolio/
├── 📂 Project 1: web scarping quotes
│   ├── quotes.py
│   └── quotes.csv
├── 📂 Project 2: web scarping countries_population
│   ├── country.py
│   └── countries.csv
├── 📂 Project 3: Web Scraping countries_capitals
│   ├── capital.py
│   ├── caps.csv
├── 📂 Project 4: Web Scraping cricketers_data
│   ├── cricket_palyers.py
│   ├── cricket_palyer.csv
├── 📂 Project 5: Web Scraping olympics_data
│   ├── main.py
│   ├── olympics_data.csv
├── README.md
```

