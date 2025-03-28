# Web Table Scraper
This simple Python script extracts tables from a given webpage and saves them as CSV files. It uses the requests library to fetch the webpage content and pandas to parse HTML tables. The extracted tables are stored in a dedicated folder inside the user's home directory.

## Features
Automatic Table Extraction: Detects and extracts all tables from an HTML page.
CSV Export: Saves each table as a CSV file for easy data analysis.
User-Friendly CLI: Prompts users for a URL and provides real-time feedback on detected tables.
Error Handling: Gracefully handles network failures and unexpected errors.
*The script will extract and save tables as CSV files in ~/scraped_data/.

## Requirements
Python 3.x
requests (pip install requests)
pandas (pip install pandas)

## Attributions
This project uses: requests (Apache License 2.0) and pandas (BSD License)
