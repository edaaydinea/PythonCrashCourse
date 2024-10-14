from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Create two D8 dice.
die1 = Die(8)
die2 = Die(8)

# Roll the dice 1,000 times and store the results.
results = [die1.roll() + die2.roll() for _ in range(1000)]

# Analyze the results.
frequencies = [results.count(value) for value in range(2, die1.num_sides + die2.num_sides + 1)]

# Visualize the results.
x_values = list(range(2, die1.num_sides + die2.num_sides + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D8 dice 1,000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d8_d8.html')
