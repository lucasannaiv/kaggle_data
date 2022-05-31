
import csv, json
from kaggle import KaggleApi

api = KaggleApi()
api.authenticate()

# Download Competition Files
api.dataset_download_file('kannan1314/amazon-stock-price-all-time', 'Amazon.csv')

def conv_json(csvFilePath, jsonFilePath):
    # Empty dict (to store json)
    data = {}

    # Open csv and convert to a dictonary
    with open(csvpath) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for rows in csvReader:
            # considering 'date' as the primarykey
            id = rows['Date']
            data[id] = rows

    # Load data dict into new json with json.dump
    with open(jsonpath, 'w') as jsonFile:
        jsonFile.write(json.dumps(data, indent=4))

# Defining the paths
csvpath = r"C:\Users\zluca\Desktop\projeto-dev\kaggle_data\Amazon.csv"
jsonpath = r"C:\Users\zluca\Desktop\projeto-dev\kaggle_data\Amazon.json"

# Call
conv_json(csvpath, jsonpath)