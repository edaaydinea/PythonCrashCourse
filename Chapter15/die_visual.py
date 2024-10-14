from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline
from save_fig import SaveFig

# Create a D6 and a D10.
die1 = Die()
die2 = Die(10)

# Make some rolls, and store results in a list.
results = []
for roll_num in range(50000):
    result = die1.roll() + die2.roll()
    results.append(result)
    
# Analyze the results.
frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
# Visualize the results.
x_values = list(range(1, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling a D6 and a D10 50,000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')

