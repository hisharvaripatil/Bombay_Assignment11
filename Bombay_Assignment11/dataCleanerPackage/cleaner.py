# File Name : cleaner.py
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
 
class DataCleaner:
    """
    Cleans the fuel purchase data by:
    - Rounding 'Gross Price' to 2 decimal places
    - Removing duplicate rows
    """
 
    def __init__(self, data_frame):
        """
        Initializes with a pandas DataFrame.
        Parameters:
            data_frame (pd.DataFrame): Raw data to clean
        """
        self.data_frame = data_frame
 
    def round_gross_price(self):
        """
        Rounds the 'Gross Price' column to exactly 2 decimal places.
        If the column doesn't exist, nothing happens.
        """
        if 'Gross Price' in self.data_frame.columns:
            self.data_frame['Gross Price'] = self.data_frame['Gross Price'].apply(lambda x: round(x, 2))
 
    def remove_duplicates(self):
        """
        Removes exact duplicate rows from the DataFrame.
        """
        initial_row_count = len(self.data_frame)
        self.data_frame.drop_duplicates(inplace=True)
        final_row_count = len(self.data_frame)
        print(f"Removed {initial_row_count - final_row_count} duplicate rows.")
 
    def get_cleaned_data(self):
        """
        Returns the cleaned DataFrame.
        Returns:
            pd.DataFrame: Cleaned data
        """
        return self.data_frame
 