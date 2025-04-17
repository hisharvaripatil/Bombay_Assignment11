# File Name : api_handler.py
# Student Name: Sharvari Patil, Rithu Aynampudi
# email:  patilsg@mail.uc.edu, aynampru@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date:   April 17, 2025
# Course #/Section:   IS 4010 Section 001
# Semester/Year:   Spring 2025
# Brief Description of the assignment: his project implements a data processing pipeline that ingests a CSV file, performs data cleaning, anomaly detection, and updates missing ZIP codes using an external API.
 
# Brief Description of what this module does: CLeaning data in python
# Citations: lecture notes, https://realpython.com/, openai.com/ChatGPT, Co-pilot
 
# Anything else that's relevant: N/A

import pandas as pd
import requests
import time
import re
 
class ZipCodeUpdater:
    def __init__(self, dataframe, api_key):
        self.df = dataframe
        self.api_key = api_key
        self.api_url = "https://api.geocod.io/v1.7/geocode"
 
    def has_zip_code(self, address):
        zip_pattern = r'\b\d{5}(?:-\d{4})?\b'
        return bool(re.search(zip_pattern, address))
 
    def update_missing_zip_codes(self):
        updated_count = 0
        addresses_to_update = []
 
        # Step 1: Find first 5 addresses without ZIP codes
        for idx, row in self.df.iterrows():
            if 'Full Address' not in row or pd.isna(row['Full Address']):
                continue
 
            full_address = str(row['Full Address']).strip()
            if not self.has_zip_code(full_address):
                addresses_to_update.append((idx, full_address))
                if len(addresses_to_update) >= 5:
                    break
 
        print(f"Found {len(addresses_to_update)} addresses without ZIP codes\n")
 
        # Step 2: Query Geocod.io
        for idx, address in addresses_to_update:
            params = {
                'q': address,
                'api_key': self.api_key
            }
 
            try:
                print(f"Processing row {idx}: {address}")
                response = requests.get(self.api_url, params=params)
 
                if response.status_code == 200:
                    data = response.json()
                    results = data.get('results', [])
                    if results:
                        zip_code = results[0].get('address_components', {}).get('zip')
                        if zip_code:
                            new_address = f"{address}, {zip_code}"
                            self.df.loc[idx, 'Full Address'] = new_address
                            print(f"Row {idx} updated → {new_address}")
                            updated_count += 1
                        else:
                            print(f"ZIP not found in response for row {idx}")
                    else:
                        print(f"No results for row {idx}")
 
                else:
                    print(f"API Error {response.status_code} for row {idx}: {response.text}")
 
            except Exception as e:
                print(f"Exception for row {idx}: {e}")
 
            time.sleep(1)
 
        print(f"\n ZIP enrichment complete. {updated_count} rows updated.\n")
        return self.df