import requests

url = "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv"
response = requests.get(url)

content = response.text.strip().splitlines()
header, *rows = content

total_records = len(rows)
unique_boroughs = set()
brooklyn_count = 0

for row in rows:
    columns = row.split(',')
    borough = columns[1].strip()
    unique_boroughs.add(borough)
    if borough == 'Brooklyn':
        brooklyn_count += 1

sorted_boroughs = sorted(unique_boroughs)

output_file = "taxi_zone_output.txt"
with open(output_file, 'w') as file:
    file.write(f"Total Number of Records: {total_records}\n")
    file.write(f"Unique Boroughs (Sorted): {', '.join(sorted_boroughs)}\n")
    file.write(f"Number of Records for Brooklyn Borough: {brooklyn_count}\n")


print(f"Analysis completed and saved to {output_file}")
import requests

url = 'https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv'

response = requests.get(url)

with open('taxi_zone_lookup.csv', 'wb') as f:
    f.write(response.content)

file = open('taxi_zone_lookup.csv', 'r')
lines = file.readlines()
file.close()

lines = lines[1:]
lines.sort()

print(len(lines))

boroughs = set()

for line in lines:
    line = line.split(',')
    boroughs.add(line[1])

print(boroughs)

brooklyn = 0

for line in lines:
    line = line.split(',')
    if line[1] == '"Brooklyn"':
        brooklyn += 1

print(brooklyn)

output = open('D:\\c400Python\\taxi_zone_output.txt', 'w') #/root/taxi_zone_output.txt 

output.write(f'Total number of records: {len(lines)}\n')
output.write(f'Unique boroughs: {boroughs}\n')
output.write(f'Number of records for Brooklyn: {brooklyn}\n')

output.close()