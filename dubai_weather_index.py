from pathlib import Path
import csv
import matplotlib.pyplot as plt

path = Path("weather_data/dubai_weather_2021_full.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)