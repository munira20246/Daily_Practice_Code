import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Functions to extract dates and PRCP(Raifalls) from the csv file.

def get_weather_data_dict(filename):
    dates, prcps = [], []
    place_name = ''

    with open(filename) as f:
        reader = csv.DictReader(f)

        for row in reader:
            if not place_name:
                 place_name = row['NAME']
        
            try:
                current_date = datetime.strptime(row['DATE'], '%Y-%m-%d')
                prcp = float(row['PRCP'])

            except ValueError:
                print(f"Missing data for {current_date}")

            else:
                dates.append(current_date)
                prcps.append(prcp)

    return dates, prcps, place_name

dhaka_file = "weather_data/dhaka_weather_2024-2025_full.csv"
mumbai_file = "weather_data/mumbai_weather_2024-2025_full.csv"

dhaka_dates, dhaka_prcps, dhaka_name = get_weather_data_dict(dhaka_file)
mumbai_dates, mumbai_prcps, mumbai_name = get_weather_data_dict(mumbai_file)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dhaka_dates, dhaka_prcps, color='red', label='Dhaka_Rainfall', alpha=0.5)
ax.fill_between(dhaka_dates, dhaka_prcps, facecolor='red', alpha=0.1)
ax.plot(mumbai_dates, mumbai_prcps, color='blue', label='Mumbai_Rainfall', alpha=0.5)
ax.fill_between(mumbai_dates, mumbai_prcps, facecolor='blue', alpha=0.1)

title = f"Daily Rainfall Record 2021\n{dhaka_name} & {mumbai_name}"
ax.set_title(title, fontsize=18)
ax.set_xlabel('Date', fontsize=10)
fig.autofmt_xdate()
ax.set_ylabel("Rainfall (mm)", fontsize=10)
ax.legend()

plt.show()



                            


