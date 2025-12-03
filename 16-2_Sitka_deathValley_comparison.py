import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Function to extract dates and temperatures from csv file.

def get_weather_data_dict(filename, location_name):
    dates, highs = [], []
    with open(filename) as f:
        reader = csv.DictReader(f)
    

        for row in reader:
            try:
                current_date = datetime.strptime(row['DATE'], '%Y-%m-%d')
                high = int(row['TMAX'])

            except ValueError:
                print(f"Missing or invalid data for {location_name} on {row['DATE']}")

            else:
                dates.append(current_date)
                highs.append(high)

    return dates, highs                

# File paths (change if needed)
sitka_file = "weather_data/sitka_weather_2021_simple.csv"
dv_file = "weather_data/death_valley_2021_simple.csv"

# Get weather data
sitka_dates, sitka_highs = get_weather_data_dict(sitka_file, 'Sitka')
dv_dates, dv_highs = get_weather_data_dict(dv_file, 'Death Valley')

# Plot the data
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(sitka_dates, sitka_highs, c='red', label='Sitka', alpha=0.5)
ax.fill_between(sitka_dates, sitka_highs, facecolor='red', alpha=0.05)
ax.plot(dv_dates, dv_highs, c='blue', label='Death Valley', alpha=0.5)
ax.fill_between(dv_dates, dv_highs, facecolor='blue', alpha=0.1)

# Format the plot 
ax.set_title("Daily High Temperatures-2021\nSitka vs Death Valley", fontsize=16)
ax.set_xlabel('', fontsize= 10)
fig.autofmt_xdate
ax.set_ylabel("Temperature (F)", fontsize=10)
ax.tick_params(labelsize= 10)
ax.legend()

plt.show()


    