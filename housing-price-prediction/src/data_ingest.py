import os
import zipfile
from abc import ABC, abstractmethod
import pandas as pd

# Define interface for Data Ingestor for differenet formats

class DataIngestor(ABC):
    @abstractmethod
    def ingest(self,file_path: str) -> pd.DataFrame:
        ''' Abstract method to ingest data from a given file.'''
        pass

class ZipDataIngestor(DataIngestor):
    def ingest(self, file_path: str) -> pd.DataFrame:
        """Extracts a .zip file and returns the content as a pandas DataFrame."""
        # Make sure file type is a .zip file
        if not file_path.endswith(".zip"):
            raise ValueError("Given File is not a .zip file...")

        with zipfile.ZipFile(file_path,"r") as zip_ref:
            zip_ref.extractall("extracted_data")

        extracted_files = os.listdir("extracted_data")
        csv_files = [f for f in extracted_files if f.endswith(".csv")]

        if len(csv_files) == 0:
            raise FileNotFoundError("No CSV file found in the extracted datad")
        if len(csv_files) > 1:
            raise ValueError("Multiple csv files found please select one....")


        csv_file_path = os.path.join("extracted_data",csv_files[0])
        df = pd.read_csv(csv_file_path)        

        return df

class DataIngestFactory:
    @staticmethod
    def get_data_ingestor(file_extension: str) ->DataIngestor:
         """Returns the appropriate DataIngestor based on file extension."""       
         if file_extension == ".zip":
             return ZipDataIngestor()
         else:
             return ValueError(f"No DataIngestor found for the given file format: {file_extension}")
         

if __name__ == "__main__":
    file_path = 'C:/Users/LAKSHYA PALIWAL/Projects/housing-price-predicition/dataarchive.zip'

    # Determine the file extension type
    file_extension = os.path.splitext(file_path)[1]

    # Determining the data ingestor to be used
    data_ingestor = DataIngestFactory.get_data_ingestor(file_extension)

    # Ingest the data and load it into a dataframe 
    df = data_ingestor.ingest(file_path)

    print(df.head())