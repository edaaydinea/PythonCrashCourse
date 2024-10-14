import matplotlib.pyplot as plt
from die import Die
from random_walk import RandomWalk
import plotly.graph_objs as go
from plotly import offline
from save_fig import SaveFig

def roll_die(num_rolls=1000):
    """Roll a D6 die a specified number of times and plot the results."""
    die = Die()
    results = [die.roll() for _ in range(num_rolls)]
    frequencies = [results.count(value) for value in range(1, die.num_sides + 1)]
    
    plt.bar(range(1, die.num_sides + 1), frequencies)
    plt.title(f"Results of rolling a D6 {num_rolls} times")
    plt.xlabel("Result")
    plt.ylabel("Frequency")
    plt.show()
    
    savefig = SaveFig()
    savefig.save_fig('d6_plot.png')
    
    

def visualize_random_walk():
    """Create and visualize a random walk using Plotly."""
    rw = RandomWalk()
    rw.fill_walk()
    
    trace = go.Scatter(x=rw.x_values, y=rw.y_values, mode='lines')
    layout = go.Layout(title='Random Walk Visualization')
    fig = go.Figure(data=[trace], layout=layout)
    
    offline.plot(fig, filename='random_walk_plotly.html')

if __name__ == "__main__":
    roll_die()
    visualize_random_walk()
