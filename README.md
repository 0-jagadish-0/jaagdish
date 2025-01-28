# 📊 Data Analyst Portfolio

Welcome to my data analyst portfolio! This repository showcases my skills, techniques, and projects in data analysis, visualization, and storytelling. Each project reflects my approach to solving real-world problems using data-driven insights.

---

## 🧑‍💻 About Me

I am a data analyst passionate about uncovering meaningful insights from data and driving informed decision-making. With expertise in data cleaning, analysis, and visualization, I strive to turn complex datasets into actionable stories.

**Key Skills:**
- Programming: Python (Pandas, NumPy, Matplotlib, Seaborn, Beautifulsoup, Requests)
- Databases: SQL (MySQL, Oracle)
- Visualization:  Power BI, Excel, Tableau
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

<details>
  <summary>**Data Analysis Projetcs**</summary>

  ### **1. Titanic Survivors Analysis**
  - **Description:** In this project, we perform a comprehensive analysis of the Titanic dataset to explore survival rates based on various factors such as class, gender, age, and embarkation port.
      The dataset is cleaned by handling missing values and then analyzed to determine patterns that might have influenced passengers' chances of survival.
     The results are visualized through different plots to provide a clear understanding of how each factor impacted survival on the Titanic.
  - **Tools Used:** Python (Pandas, Numpy, Seaborn, Matplotlib)
  - **Visualiations:** 
    - Created five key visualizations to highlight insights:
    - Overall Survivors: Bar chart showing the percentage of survivors versus non-survivors.
    - Survivors by Gender: Comparison of survival rates between males and females, highlighting significant gender differences.
    - Survivors by Age Group: Age groups (e.g., children, adults, elderly) and their respective survival rates visualized using a histogram or box plot.
    - Survivors by Class: A breakdown of survival rates across first, second, and third-class passengers using a bar plot.
    - Survivors by Embarkation Port: Analysis of survival rates based on the embarkation ports (Southampton, Cherbourg, Queenstown) using a bar or pie chart.
  - **Challenges Solved:**
    - Handling Missing Data: Applied techniques like imputation and exclusion for missing values in the age and embarkation columns.
    - Balancing Data for Visualization: Used percentage-based normalization to avoid misleading interpretations due to class imbalances.
  - **Skills Demonstrated:**
    - Data preprocessing and cleaning.
    - Data analysis and interpretation.
    - Data visualization using Seaborn and Matplotlib.
    - Communicating findings effectively through visual and textual narratives.
  - [Explore Project](https://github.com/0-jagadish-0/jagadish/blob/b69bc9c0b4b810d1510cd95e4ecb688694947e53/Data%20Anlysis%20Titanic%20Survivors/main.ipynb)
  - 
  ### **2. Simple Trading Strategy Using Facebook stock data**
  - **Description:** This project demonstrates a simple trading strategy using historical stock data for Facebook (Meta Platforms).
      The strategy leverages moving averages to generate buy signals and evaluates the overall performance of the strategy over time.
      It is designed to help understand basic financial analysis concepts and Python programming for data manipulation and visualization.
  - **Tools Used:** Python (Pandas, Numpy, Seaborn, Matplotlib)
  - **Key Features:** 
    - Interactive Visualization: Easily interpretable charts highlighting the strategy’s signals.
    - Customizable Strategy: Modify the moving average parameters to test different trading strategies.
    - Beginner-Friendly Code: Clear, well-documented code for ease of understanding and learning.
  - **Skills Demonstrated:**
    - Data preprocessing and cleaning.
    - Data analysis and interpretation.
    - Data visualization using Seaborn and Matplotlib.
    - Communicating findings effectively through visual and textual narratives.
  - [Explore Project](https://github.com/0-jagadish-0/jagadish/blob/a013dddd8c3e1f741487c1380ebe649319f48cee/facebook%20stock%20strategy/main.ipynb)

</details>
    
<details>
  <summary>** Dash-Boards **</summary>

  ### **1. Customer data analysis**
  - **Description:** The goal of this project was to create a comprehensive dashboard that provides insights into various revenue metrics,
     offering a detailed view of the revenue performance across multiple dimensions. The dashboard aims to empower the marketing team with actionable insights into key business drivers.
  - **Tools Used:** Tableau
  - **Visualiations:** 
    - Revenue by State: A visual representation of revenue generated from different states, helping the team identify high and low-performing regions.
    - Revenue by Month: An analysis of monthly revenue trends, enabling the marketing team to track seasonal patterns and plan campaigns accordingly.
    - Revenue by Age Group: A breakdown of revenue based on customer age groups, offering valuable insights into which demographics are driving the most revenue.
    - Discount Percentage vs. Quantity Sold: A correlation analysis to explore how discount percentages impact sales volume, helping to refine pricing strategies.
    - Revenue Percentage by Region: A geographic breakdown of revenue contributions by different regions, aiding regional marketing and sales teams.
    - Revenue by Category per Gender: A comparison of revenue by product category segmented by gender, enabling more targeted and personalized marketing efforts.
  - **Features of the Dashboard::**
    - Interactive Filters: Users can interact with the dashboard by applying filters such as state, gender, and category to drill down into specific insights.
    - Dynamic Visualizations: Includes bar charts, line graphs, pie charts, and maps for a diverse representation of the data.
    - Revenue Trends Over Time: A line graph for tracking revenue growth across different months, allowing for easy identification of growth or decline patterns.
    - Cross-Tab Views: Ability to view segmented data across multiple dimensions such as age, gender, and region for more granular insights.
  - **Outcomes & Impact:**
      The dashboard enabled the marketing team to identify high-performing regions and demographics, which helped tailor marketing strategies and improve resource allocation.
      Insights into the relationship between discount percentage and quantity sold allowed the pricing strategy to be optimized, potentially increasing overall sales without sacrificing profit margins.
      The regional and gender-specific breakdowns enabled the development of more personalized marketing campaigns, resulting in higher engagement and conversion rates.
  - [Explore Project](https://public.tableau.com/views/customeranalysis_17378026947060/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

### **2. Sales Analysis Dashboard**  
- **Description:**  The goal of this project was to build a comprehensive and interactive dashboard that provides detailed insights into sales performance metrics.
  The dashboard allows businesses to understand key drivers of revenue, profit, and market trends, enabling data-driven decisions to optimize sales strategies and boost profitability.  
- **Tools Used:**  
   - Tableau (for dashboard visualization)  
   - MySQL (for data extraction)  
   - Python (for automated data cleaning and preprocessing using Pandas)  
- **Visualizations:**  
   - **Revenue by Market:** A breakdown of revenue by market, helping identify the most profitable markets and revenue contributions.  
   - **Profit Margin Percentage by Market:** A visual analysis of profit margin percentages across different markets to pinpoint high-margin segments.  
   - **Revenue Trend Analysis:** A line graph showing revenue growth trends over time (monthly/quarterly/yearly) to uncover seasonal patterns and growth areas.  
   - **Profit Margin Contribution by Customer:** Insights into customers contributing the most to overall profit, helping prioritize customer-centric strategies.  
   - **Top Revenue Contributors by Customer:** A visual breakdown of top customers based on their revenue contributions.  
   - **Revenue by Product Category:** Analysis of product category performance across different dimensions such as market, region, and gender.  
- **Features of the Dashboard:**  
   - **Interactive Filters:** Users can apply filters (e.g., market, region, customer segment) to explore specific insights and drill down into granular details.  
   - **Dynamic Visualizations:** Includes bar charts, line graphs, and pie charts for intuitive data representation.  
   - **Profit and Revenue Comparison:** A side-by-side view of profit and revenue metrics to identify areas of inefficiency or opportunities for improvement.  
   - **Cross-Tab Views:** Enables detailed analysis across multiple dimensions, such as product category and customer demographics.  
   - **Real-Time Insights:** Updated metrics for accurate and timely decision-making.  
- **Outcomes & Impact:**  
   - Enabled the identification of high-performing markets, product categories, and customer segments, leading to targeted sales and marketing strategies.  
   - Provided insights into profit margin contributors, helping optimize resource allocation and pricing strategies.  
   - Highlighted revenue trends, allowing for better forecasting and strategic planning.  
   - Improved decision-making with actionable, data-driven insights tailored to business needs.
   - [Explore Project](https://public.tableau.com/views/sales_data_analysis_17379131554170/summary?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)


</details>


