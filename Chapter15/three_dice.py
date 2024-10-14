from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Create three D6 dice.
die1 = Die()
die2 = Die()
die3 = Die()

# Roll the dice and store the results.
results = [die1.roll() + die2.roll() + die3.roll() for _ in range(5000)]

# Analyze the results.
frequencies = [results.count(value) for value in range(3, die1.num_sides * 3 + 1)]

# Visualize the results.
x_values = list(range(3, die1.num_sides * 3 + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling three D6 dice 5,000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='three_d6.html')
