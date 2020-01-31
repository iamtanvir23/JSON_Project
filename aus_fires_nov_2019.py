#import plotly
import json

in_file = open('eq_data_1_day_m1.json','r')
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

# List Magnitude of Each Earthquake
for eq in list_of_eqs:
    mag = eq['properties']['mag']
    lon = eq['geometry']['coordinates'][0]
    lat = eq['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

# Print Magnitude of First 10 Values
print(mags[:10])
print(lons[:10])
print(lats[:10])

from plotly.graph_objs import Scattergeo,Layout
from plotly import offline

data = [Scattergeo(lon=lons,lat=lats)]
my_layout = Layout(title="Global Earthquakes")
fig = {'data':data, 'layout':my_layout}
offline.plot(fig,filename='global_earthquakes.html')