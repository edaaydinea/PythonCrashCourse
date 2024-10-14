from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Create a D6 and a D10.
die1 = Die()
die2 = Die(10)

# Roll the dice and store the multiplication results.
results = [die1.roll() * die2.roll() for _ in range(5000)]

# Analyze the results.
max_result = die1.num_sides * die2.num_sides
frequencies = [results.count(value) for value in range(1, max_result + 1)]

# Visualize the results.
x_values = list(range(1, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of multiplying rolls of a D6 and a D10, 5,000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10_multiplication.html')
