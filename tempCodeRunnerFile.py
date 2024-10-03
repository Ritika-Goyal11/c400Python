import requests
url = "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv"
response = requests.get(url)
dataset = 'taxi_zone_lookup.csv'

