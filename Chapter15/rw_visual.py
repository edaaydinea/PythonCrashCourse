import matplotlib.pyplot as plt
from save_fig import SaveFig
from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk(50_000)
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9), dpi=128)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)
    
    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    
    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # Save the image
    savefig = SaveFig()
    savefig.save_fig('rw_visual.png')
    
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break