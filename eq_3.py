# Josh Jacobsen - MW 2:30pm
# JSON_Project

# - - - - Earthquakes Practice - - - - 

import json

in_file = open('eq_data_30_day_m1.json','r')
outfile = open('readable_eq_data.json','w')

# Load as Dictionary
eq_data = json.load(in_file)

# Print Type
print(type(eq_data))

# Dump File Contents in a Readable Way
json.dump(eq_data,outfile,indent=4)

# List of Earthquakes
list_of_eqs = eq_data['features']

print(type(list_of_eqs))
print(len(list_of_eqs))

# List for Earthquake Magnitudes, Longitudes, and Ladatudes
mags = []
lons = []
lats = []
hover_texts = []

# List Magnitude of Each Earthquake
for eq in list_of_eqs:
    mag = eq['properties']['mag']
    lon = eq['geometry']['coordinates'][0]
    lat = eq['geometry']['coordinates'][1]
    
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

    title = eq['properties']['title']
    hover_texts.append(title)

# Print Magnitude of First 10 Values
print(mags[:10])
print(lons[:10])
print(lats[:10])

from plotly.graph_objs import Scattergeo,Layout
from plotly import offline

# data = [Scattergeo(lon=lons,lat=lats)]

data = [{'type': 'scattergeo',
        'lon': lons,
        'lat': lats,
        'text': hover_texts,
        'marker':{
            'size':[5*mag for mag in mags],
            'color': mags,
            'colorscale': 'Viridis',
            'reversescale': True,
            'colorbar': {'title':'Magnitude'}
            }
        }]

my_layout = Layout(title="Global Earthquakes")
fig = {'data':data, 'layout':my_layout}
offline.plot(fig,filename='global_earthquakes.html')