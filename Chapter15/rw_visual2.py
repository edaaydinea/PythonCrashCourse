import matplotlib.pyplot as plt
from save_fig import SaveFig
from modified_random_walks import RandomWalk, RandomWalk2, RandomWalk3


def random_walk(rw, filename):
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
    savefig.save_fig(f'modified_rw_visual{filename}.png')

    
if __name__ == '__main__':

    # Make a random walk, and plot the points.
    rw1 = RandomWalk(50_000)
    rw2 = RandomWalk2(50_000)
    rw3 = RandomWalk3(50_000)

    random_walk(rw1, '1')
    random_walk(rw2, '2')
    random_walk(rw3, '3')

