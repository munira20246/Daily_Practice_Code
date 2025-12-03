from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

def get_weather_data(path, date_index, high_index, low_index, place_name_index ):
    ''''Get the highs and lows from a data file.'''
    dates, highs, lows = [], [], []
    place_name = ''

    lines = path.read_text().splitlines()
    reader = csv.reader(lines)
    header_row = next(reader)

    for row in reader:
        if not place_name:
            place_name = row[place_name_index]

        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')

        try:
            high = int(row[high_index])
            low = int(row[low_index])

        except ValueError:
            print(f"Missing data for {current_date}") 

        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    return dates, highs, lows, place_name

    
# Get the weather data from Dhaka.
dhaka_path = Path("weather_data/dhaka_weather_2024-2025_full.csv")

dhaka_dates, dhaka_highs, dhaka_lows, dhaka_name = get_weather_data(dhaka_path, date_index=2, high_index=5, low_index=6, place_name_index=1)

# Get weather data from Mumbai.
mumbai_path = Path("weather_data/mumbai_weather_2024-2025_full.csv")

mumbai_dates, mumbai_highs, mumbai_lows, mumbai_name = get_weather_data(mumbai_path, date_index=2, high_index=5, low_index=6, place_name_index=1)

# Plot the both cities weather data.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

# Dhaka Plot
ax.plot(dhaka_dates, dhaka_highs, color='green', label='Dhaka_High_Temperature', alpha=0.5)
ax.plot(dhaka_dates, dhaka_lows, color='blue', label='Dhaka_Low_Temperature', alpha=0.5)
ax.fill_between(dhaka_dates, dhaka_highs, dhaka_lows, facecolor='green', alpha=0.1)


# Mumbai Plot
ax.plot(mumbai_dates, mumbai_highs, color='red', label='Mumbai_High_Temperature', alpha=0.5)
ax.plot(mumbai_dates, mumbai_lows, color='purple', label='Mumbai_Low_Temperatur', alpha=0.5)
ax.fill_between(mumbai_dates, mumbai_highs, mumbai_lows, facecolor='purple', alpha=0.1)

# Format the plot
title = f"Daily Temperature-(2024-2025)\n{dhaka_name} & {mumbai_name}"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=12)
fig.autofmt_xdate()
ax.set_ylabel("Temperatures (F)", fontsize=12)
ax.tick_params(labelsize=10)
ax.set_ylim(10, 140)
ax.legend()

plt.show()
