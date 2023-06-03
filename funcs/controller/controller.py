import pandas as pd
import os

TMP_DIR = './tmp/'

def main(file):
    # Create dataframe from CSV
    df = pd.read_csv(file)

    # Ignore Unnamed columns
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    # Get filename
    filename = file.filename[:-4]

    # Get columns
    columns = list(df.columns)

    # Remove file if exists, avoid duplication
    file_path = os.path.join(TMP_DIR, file.filename)
    if os.path.exists(file_path):
        os.remove(file_path)

    # Store the received file
    df.to_csv(file_path)

    return {"filename": filename, "columns":columns}


def get_value(file, column_index):
    # Define filepath
    file_path = os.path.join(TMP_DIR, file+'.csv')

    # Read file if exists
    if os.path.exists(file_path):
        df   = pd.read_csv(file_path)
        df   = df.loc[:, ~df.columns.str.contains('^Unnamed')]
        data = sorted(df[df.columns[column_index]].unique().tolist())

        # Create list of html options
        options = [f"<option value='{item}'>{item}</option>" for item in data]
        return {"message": options}
    else:
        raise Exception('File not found.')

def delete_file(filename):
    # Define filepath
    file_path = os.path.join(TMP_DIR, filename+'.csv')

    # Remove file if exists
    if os.path.exists(file_path):
        os.remove(file_path)

    return {"message": "success"}