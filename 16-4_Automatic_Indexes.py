from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('weather_data/san_francisco_weather_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

date_index = header_row.index('DATE')
high_index = header_row.index('TMAX')
low_index = header_row.index('TMIN')
name_index = header_row.index('NAME')

# Extracts dates and high & low temperatures
dates, highs, lows = [], [], []
place_name = ""

for row in reader:
    # Grab the station name, if it's not already set.
    if not place_name:
        place_name = row[name_index]

    current_date = datetime.strptime(row[date_index], '%Y-%m-%d')

    try:
        high = int(row[high_index])
        low = int(row[low_index])
    except ValueError:
        print(f"Missing data of {current_date}")

    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)  

# Plot the high and low temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='blue', label='High_Temperature', alpha=0.5)
ax.plot(dates, lows, color='red', label='Low_Temperature', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format the data
title = f"Daily High & Low Temperatures-2021\n{place_name}"
ax.set_title(title, fontsize=16)
ax.set_xlabel('', fontsize=12)
fig.autofmt_xdate()
ax.set_ylabel("Temperatures (F)", fontsize=12)
ax.tick_params(labelsize=10)
ax.legend()

plt.show()
