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