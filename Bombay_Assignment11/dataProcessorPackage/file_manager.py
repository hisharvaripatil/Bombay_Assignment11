# File Name : file_manager.py
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

 
import os
import pandas as pd
 
class FileHandler:
    """
    Handles reading from and writing to CSV files
    within the Data folder of the project.
    """
 
    def __init__(self):
        
        self.data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Data')
 
    def load_csv(self, filename):
        """
        Loads a CSV file from the Data directory and returns a DataFrame.
        Parameters:
            filename (str): Name of the file to read (e.g., 'fuelPurchaseData.csv')
        Returns:
            pd.DataFrame: The loaded CSV data
        """
        path = os.path.join(self.data_dir, filename)
        if not os.path.exists(path):
            raise FileNotFoundError(f"File not found: {path}")
        return pd.read_csv(path)
 
    def save_csv(self, df, filename):
        """
        Saves a DataFrame to a CSV file in the Data directory.
        Parameters:
            df (pd.DataFrame): The data to save
            filename (str): The name of the output file (e.g., 'cleanedData.csv')
        """
        path = os.path.join(self.data_dir, filename)
        df.to_csv(path, index=False)
 
    def ensure_data_folder(self):
        """
        Creates the Data folder if it doesn't already exist.
        """
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
 
