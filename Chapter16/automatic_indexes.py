import pandas as pd
import matplotlib.pyplot as plt
from save_fig import SaveFig

def get_temperature_indexes(header):
    tmin_index = header.index('TMIN')
    tmax_index = header.index('TMAX')
    return tmin_index, tmax_index

# Load data and header row
sitka_data = pd.read_csv('data/sitka_weather_2018_simple.csv')
header = list(sitka_data.columns)

# Automatically find TMIN and TMAX indexes
tmin_index, tmax_index = get_temperature_indexes(header)

# Extract TMIN and TMAX data
sitka_dates = pd.to_datetime(sitka_data['DATE'])
sitka_tmin = sitka_data.iloc[:, tmin_index]
sitka_tmax = sitka_data.iloc[:, tmax_index]

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(sitka_dates, sitka_tmin, label='TMIN', color='blue', alpha=0.6)
plt.plot(sitka_dates, sitka_tmax, label='TMAX', color='red', alpha=0.6)

# Set plot title dynamically based on station name
station_name = "Sitka"
plt.title(f"Temperature Data: {station_name} (2018)", fontsize=16)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Temperature (°F)", fontsize=14)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()


# Save the plot
save_fig = SaveFig()
save_fig.save_fig("automatic_indexes.png")