import json
from pathlib import Path

class DataReader:
    FILE_PATH = Path("testdata/testdata.json")

    @staticmethod
    def get_testdata():
        with open(DataReader.FILE_PATH) as file:
            return json.load(file)
    
    @staticmethod
    def get_search_value():
        return DataReader.get_testdata()["testdata"]["search_value"]
    
    @staticmethod
    def get_product_name():
        return DataReader.get_testdata()["testdata"]["product_name"]
    



    
