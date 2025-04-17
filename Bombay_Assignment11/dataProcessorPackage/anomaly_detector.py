# File Name : anomaly_detector.py
# Student Name: Sharvari Patil, Rithu Aynampudi
# email:  patilsg@mail.uc.edu, aynampru@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date:   April 17, 2025
# Course #/Section:   IS 4010 Section 001
# Semester/Year:   Spring 2025
# Brief Description of the assignment: his project implements a data processing pipeline that ingests a CSV file, performs data cleaning, anomaly detection, and updates missing ZIP codes using an external API.
 
# Brief Description of what this module does: CLeaning data in python
# Citations:  lecture notes, https://realpython.com/, openai.com/ChatGPT, Co-pilot
 
# Anything else that's relevant: N/A
 
import pandas as pd
import os
 
class AnomalyDetector:
    def __init__(self, dataframe, anomalies_file):
        self.dataframe = dataframe
        self.anomalies_file = anomalies_file
 
    def detect_anomalies(self):
        
        anomalies = self.dataframe[self.dataframe['Fuel Type'].str.strip().str.lower() == 'pepsi']
        
        cleaned_data = self.dataframe[self.dataframe['Fuel Type'].str.strip().str.lower() != 'pepsi']
 
        
        os.makedirs("Data", exist_ok=True)
        anomalies.to_csv(os.path.join("Data", self.anomalies_file), index=False)
 
        print(f"Detected {len(anomalies)} rows with Pepsi")
        print(f"Returning {len(cleaned_data)} rows after cleaning")
 
        return cleaned_data