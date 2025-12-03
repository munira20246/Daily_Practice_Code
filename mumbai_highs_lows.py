from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path("weather_data/mumbai_weather_2024-2025_full.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

dates, highs, lows = [], [], []
place_name = ''

for row in reader:
    if not place_name:
        place_name = row[1]

    current_date = datetime.strptime(row[2], '%Y-%m-%d')

    try:
        high = int(row[5])
        low = int(row[6])
    except ValueError:
        print(f"Missing data for {current_date}")   

    else:
        dates.append(current_date)
        highs.append(high) 
        lows.append(low)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', label='High_Temperatures', alpha=0.5)
ax.plot(dates, lows, color='blue', label='Low_Temperatures', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

title = f"Daily High & Low Temperatures-(2024-2025)\n{place_name}"
ax.set_title(title, fontsize=18)
ax.set_xlabel('', fontsize=10)
fig.autofmt_xdate()
ax.set_ylabel('Temperatures (F)', fontsize=10)
ax.tick_params(labelsize=9)
ax.legend()

plt.show()