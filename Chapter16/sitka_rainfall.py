import pandas as pd
import matplotlib.pyplot as plt
from save_fig import SaveFig

# Load the data
filename = 'data/sitka_weather_2018_simple.csv'
data = pd.read_csv(filename)

# Extract rainfall data
rainfall = data['PRCP']

# Extract dates for plotting
dates = pd.to_datetime(data['DATE'])

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(dates, rainfall, color='blue', alpha=0.5)
plt.fill_between(dates, rainfall, color='blue', alpha=0.2)

# Set plot title and labels
plt.title("Daily Rainfall in Sitka (2018)", fontsize=16)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Rainfall (inches)", fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()

save_fig = SaveFig()
save_fig.save_fig('sitka_rainfall.png')
