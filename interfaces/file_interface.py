import pandas as pd
import os

from core.exception import ItemNotFound

class FileInterface:

    def __init__(self) -> None:
        self.tmp_dir = os.environ.get('TMP_DIR')


    def save_file(self, file):
        # Create dataframe from CSV
        df = pd.read_csv(file)

        # Ignore Unnamed columns
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

        # Get filename
        filename = file.filename
        file_path = os.path.join(self.tmp_dir, filename)

        # Remove file if exists, avoid duplication
        self.delete_file(filename)

        # Store the received file
        df.to_csv(file_path)

        return filename
    

    def read_file(self, filename):
        # Define filepath
        file_path = os.path.join(self.tmp_dir, filename)

        # Read file if exists
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
            return df
        else:
            raise ItemNotFound('File not found.')
        

    def delete_file(self, filename):
        # Define filepath
        file_path = os.path.join(self.tmp_dir, filename)

        # Remove file if exists
        if os.path.exists(file_path):
            os.remove(file_path)
    

    def get_columns(self, filename):
        # Read file
        df = self.read_file(filename)
        return list(df.columns)


    def get_columns_content(self, filename, column):
        # Define filepath
        file_path = os.path.join(self.tmp_dir, filename)

        # Read file if exists
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
            content = sorted(df[column].unique().tolist())

            return content
        
        else:
            raise ItemNotFound('File not found.')

