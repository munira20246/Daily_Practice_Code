from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path("weather_data/sitka_weather_2021_full.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

rainfalls, dates = [] , []

for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    rainfall = float(row[5])
    dates.append(current_date)
    rainfalls.append(rainfall)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, rainfalls, color='red')

ax.set_title("Daily Rainfall, 2021", fontsize=20)
ax.set_xlabel('', fontsize=12)
fig.autofmt_xdate()

ax.set_ylabel("Rainfalls", fontsize=12)
ax.tick_params(labelsize=12)

plt.show()
