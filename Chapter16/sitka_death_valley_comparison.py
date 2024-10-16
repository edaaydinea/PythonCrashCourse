import pandas as pd
import matplotlib.pyplot as plt
from save_fig import SaveFig

# Load the data
sitka_data = pd.read_csv('data/sitka_weather_2018_simple.csv')
death_valley_data = pd.read_csv('data/death_valley_2018_simple.csv')

# Extract dates and temperatures
sitka_dates = pd.to_datetime(sitka_data['DATE'])
sitka_temps = sitka_data['TMAX']

death_valley_dates = pd.to_datetime(death_valley_data['DATE'])
death_valley_temps = death_valley_data['TMAX']

# Create the plot
plt.figure(figsize=(10, 6))

# Sitka
plt.plot(sitka_dates, sitka_temps, color='blue', alpha=0.6, label='Sitka')

# Death Valley
plt.plot(death_valley_dates, death_valley_temps, color='red', alpha=0.6, label='Death Valley')

# Set identical y-axis range
plt.ylim(0, 120)

# Set plot title and labels
plt.title("Temperature Comparison: Sitka vs. Death Valley (2018)", fontsize=16)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Temperature (°F)", fontsize=14)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

save_fig = SaveFig()
save_fig.save_fig('sitka_death_valley_comparison.png')
