# File Name : main.py
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

from dataProcessorPackage.anomaly_detector import *
from dataCleanerPackage.api_handler import * 
from dataCleanerPackage.cleaner import * 
from dataProcessorPackage.anomaly_detector import * 
from dataProcessorPackage.file_manager import *
 

def main():
 
    # STEP 1: Load the original fuel purchase data from the Data folder
 
    print("Step 1: Loading the original data from the 'Data' folder...")
 
    fh = FileHandler()
 
    df = fh.load_csv("fuelPurchaseData.csv")
 
    print(f"Original data loaded: {len(df)} rows")
    # STEP 2: Clean the data
 
    print("\nStep 2: Cleaning the data by rounding gross price and removing duplicates...")
 
    cleaner = DataCleaner(df)
    cleaner.round_gross_price()
    cleaner.remove_duplicates()
    cleaned_df = cleaner.get_cleaned_data()
 
    print(f"Data cleaned: {len(cleaned_df)} rows remaining after cleaning")
    # STEP 3: Detect anomalies (non-fuel rows like Pepsi)
 
    print("\nStep 3: Detecting anomalies such as non-fuel purchases (e.g., Pepsi)...")
 
    anomaly_detector = AnomalyDetector(cleaned_df, "dataAnomalies.csv")
 
    fuel_only_df = anomaly_detector.detect_anomalies()
 
    print(f"Anomalies detected: {len(cleaned_df) - len(fuel_only_df)} rows removed (e.g., Pepsi)")
    # STEP 4: Fill in missing ZIP codes using API
 
    print("\nStep 4: Enriching data by filling in missing ZIP codes using the external API...")
 
    zip_updater = ZipCodeUpdater(fuel_only_df, "f8bf6bbbbe78f07bfbfebfa8f0f66be10fb07bf")
 
    updated_df = zip_updater.update_missing_zip_codes()
 
    print(f"Missing ZIP codes enriched: {len(fuel_only_df) - len(updated_df)} rows updated with ZIP codes")
    # STEP 5: Save final cleaned + enriched data
 
    print("\nStep 5: Saving the final cleaned and enriched data...")
 
    fh.save_csv(updated_df, "cleanedData.csv")
 
    print("Data processing pipeline completed!")
    print("Output saved to 'Data/cleanedData.csv'")
 
if __name__ == "__main__":
 
    main()
 