import matplotlib.pyplot as plt
from save_fig import SaveFig
from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk(5000)
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9), dpi=128)
    point_numbers = range(rw.num_points)
    plt.plot(rw.x_values, rw.y_values, linewidth=1)
    
    # Emphasize the first and last points.
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    
    # Remove the axes.
    plt.axis('off')

    # Save the image
    savefig = SaveFig()
    savefig.save_fig('molecular_motion.png')
    
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break