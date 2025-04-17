import pandas as pd
from dataCleanerPackage.api_handler import APIHandler
from dataProcessorPackage.anomaly_detector import AnomalyDetector
from dataProcessorPackage.file_manager import FileManager

class Cleaner:
    def __init__(self, input_file, cleaned_file, anomalies_file):
        self.input_file = input_file
        self.cleaned_file = cleaned_file
        self.anomalies_file = anomalies_file
        self.api = APIHandler()

   