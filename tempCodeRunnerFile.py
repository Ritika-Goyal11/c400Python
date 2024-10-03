import requests

url = "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv"
dataset = requests.get(url)

import requests
import csv

# Step 1: Download the CSV dataset
url = "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv"
response = requests.get(url)

# Save the CSV content to a local file
csv_file = "taxi_zone_lookup.csv"
with open(csv_file, 'wb') as file:
    file.write(response.content)

