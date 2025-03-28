import os
import requests
import pandas as pd
from io import StringIO

def fetch_and_parse(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            tables = pd.read_html(StringIO(response.text))
            print(f"Found {len(tables)} tables.")

            output_dir = os.path.expanduser("~/scraped_data")
            os.makedirs(output_dir, exist_ok=True)

            for i, df in enumerate(tables):
                print(f"\nTable {i+1} Preview:")
                print(df.head())

                file_path = os.path.join(output_dir, f"scraped_table_{i+1}.csv")
                df.to_csv(file_path, index=False)
                print(f"\nTable {i+1} saved to \"{file_path}\"!")
            
            return tables
        else:
            print(f"Fetch failed. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

target_url = input("Enter URL with tables: ")
fetch_and_parse(target_url)