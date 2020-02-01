
import json
import csv


file_2019_fires = open('MODIS_C6_Australia_NewZealand_MCD14DL_NRT_2019331.txt','r')
data_2019_fires = csv.reader(file_2019_fires,delimiter=',')



header_row = next(data_2019_fires)

#Shows that the header row is a list
# print(type(header_row))

#Loop through columns and print name and index
# for index,column_header in enumerate(header_row):
#     print(index,column_header)


# List for Fire Brightness, Longitudes, and Ladatudes
brights = []
lons = []
lats = []
for row in data_2019_fires:
    lats.append(row[0])
    lons.append(row[1])
    brights.append(int(float(row[2])))

# Print Magnitude of First 10 Values
print(brights[:10])
print(lons[:10])
print(lats[:10])

import plotly
from plotly.graph_objs import Scattergeo,Layout
from plotly import offline

scl = [0,"rgb(150,0,90)"],[0.125,"rgb(0, 0, 200)"],[0.25,"rgb(0, 25, 255)"],\
[0.375,"rgb(0, 152, 255)"],[0.5,"rgb(44, 255, 150)"],[0.625,"rgb(151, 255, 0)"],\
[0.75,"rgb(255, 234, 0)"],[0.875,"rgb(255, 111, 0)"],[1,"rgb(255, 0, 0)"]

data = [Scattergeo(
        lon=lons,
        lat=lats,
        marker = dict(
            color = brights,
            colorscale = 'Viridis',
            reversescale = True,
            line=dict(width=1,color='White'),
            size = 12,
            colorbar = dict(
                titleside = "top",
                title='Brightness'
                )
            )
    )]

my_layout = Layout(title="November 2019 Australia Fires",geo = dict(
            fitbounds="locations",            
            showland = True,
            landcolor = "rgb(229, 236, 246)",

        ))
fig = {'data':data, 'layout':my_layout}


offline.plot(fig,filename='November 2019 Australia Fires.html')