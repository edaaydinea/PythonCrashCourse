import json

from plotly.graph_objs import Scattergeo, Layout, Figure
from plotly import offline
from save_fig import SaveFig

# Explore the structure of the data.
filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)
    
all_eq_dicts = all_eq_data['features']
    
# Extract magnitudes, longitudes, latitudes, and titles.
mags, lons, lats, hover_texts = [], [], [], []

for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)
    
title = all_eq_data['metadata']['title']

my_layout = Figure(title=title,
                   geo =dict(showland=True))

fig = Figure(data=[Scattergeo(lon=lons, lat=lats, text=hover_texts, marker=dict(size=mags, color='red'))], layout=my_layout)


save_fig = SaveFig()
save_fig.save_fig(fig, "automated_title.png")