import csv
from datetime import datetime

import matplotlib.pyplot as plt

# Function to extracts dates and temperatures from csv files.

def get_weather_data_dict(filename, location_name):
    dates, highs, lows = [], [], []
    
    with open(filename) as f:
        reader = csv.DictReader(f)


        for row in reader:
            try:
                current_dates = datetime.strptime(row['DATE'], '%Y-%m-%d')
                high =  int(row['TMAX'])
                low = int(row['TMIN'])

            except ValueError: 
                print(f"Missing or invalid data for {location_name} on {row['DATE']}")

            else:
                dates.append(current_dates)
                highs.append(high)
                lows.append(low)

    return dates, highs, lows
                   
# File Path
francisco_file = "weather_data/san_francisco_weather_2021_full.csv"
sitka_file = "weather_data/sitka_weather_2021_simple.csv"

# Get weather data

francisco_dates, francisco_highs, francisco_lows = get_weather_data_dict(francisco_file, 'San Francisco')
sitka_dates, sitka_highs, sitka_lows = get_weather_data_dict(sitka_file, 'Sitka')

# Plot the data
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(francisco_dates, francisco_highs, color='red', label='San_Francisco_High', alpha=0.5)
ax.plot(francisco_dates, francisco_lows, color='blue', label='San_Francisco_Low', alpha=0.5)
ax.fill_between(francisco_dates, francisco_highs, francisco_lows, facecolor='blue', alpha=0.1)

ax.plot(sitka_dates, sitka_highs, color='orange', label='Sitka_High', alpha=0.5)
ax.plot(sitka_dates, sitka_lows, color='green', label='Sitka_Low', alpha=0.5)
ax.fill_between(sitka_dates, sitka_highs, sitka_lows, facecolor='green', alpha=0.1)

# Format the plot
ax.set_title("Daily High & Low Temperatures-2021\nSan_Francisco vs Sitka", fontsize=20)
ax.set_xlabel('', fontsize=10)
fig.autofmt_xdate
ax.set_ylabel("Temperatures (F)", fontsize=10)
ax.tick_params(labelsize=10)
ax.legend()

plt.show()