
import csv, os
from pathlib  import Path


def load_data():
    files_path = os.path.join(Path(os.getcwd()).parent, 'files')
    files = {}
    for file in os.listdir(files_path):
        file_path = os.path.join(files_path, file)
        with open(file_path, 'r') as csv_file:
            data = list(csv.reader(csv_file))[0]
            file_number = file[:file.find(".")]
            files[file_number] = data
    return files


if __name__ == "__main__":
    print(load_data())