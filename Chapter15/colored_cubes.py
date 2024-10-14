#! python3
# cubes.py - A number raised to the third power is a cube. Plot the first five cubic numbers, and then plot the first 5000 cubic numbers. Apply a colormap to your cubes plot.

import matplotlib.pyplot as plt
from save_fig import SaveFig

input_values = list(range(1, 5001))
cubes = [x**3 for x in input_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
scatter = ax.scatter(input_values, cubes, c=cubes, cmap=plt.cm.viridis, s=10)

# Set chart title and label axes
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', labelsize=14)

# Add a color bar
colorbar = plt.colorbar(scatter)
colorbar.set_label('Cube of Value', fontsize=14)

# Save the image
savefig = SaveFig()
savefig.save_fig('colored_cubes.png')