from pathlib import Path
import csv

path = Path("weather_data/mumbai_weather_2024-2025_full.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)
