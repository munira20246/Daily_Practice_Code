from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path("weather_data/dubai_weather_2021_full.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_column = next(reader)

dates, highs, lows = [], [], []
place_name = ''

for row in reader:

    if not place_name:
        place_name = row[1]

    current_date = datetime.strptime(row[5], '%Y-%m-%d')
    try:
        high = int(row[10])
        low = int(row[12])

    except ValueError:
        print(f"Missing or invalid data for {current_date}")

    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Plot the figure.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', label='High_Temperatures', alpha=0.5)
ax.plot(dates, lows, color='green', label='Low_Temperatures', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format the figure.
title = f"Daily High & Low Temperatures-2021\n{place_name}"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=12)
fig.autofmt_xdate
ax.set_ylabel("Temperatures (F)", fontsize=12)
ax.tick_params(labelsize=10)
ax.legend()

plt.show()