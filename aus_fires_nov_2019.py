#import plotly
import json
import csv

# in_file = open('eq_data_1_day_m1.json','r')
# outfile = open('readable_eq_data.json','w')

file_2019_fires = open('MODIS_C6_Australia_NewZealand_MCD14DL_NRT_2019331.txt','r')
data_2019_fires = csv.reader(file_2019_fires,delimiter=',')

# # Load as Dictionary
# eq_data = json.load(in_file)

# # Print Type
# print(type(eq_data))

# # Dump File Contents in a Readable Way
# json.dump(eq_data,outfile,indent=4)

# # List of Earthquakes
# list_of_eqs = eq_data['features']

# print(type(list_of_eqs))
# print(len(list_of_eqs))

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

# import plotly
from plotly.graph_objs import Scattergeo,Layout
from plotly import offline

scl = [0,"rgb(150,0,90)"],[0.125,"rgb(0, 0, 200)"],[0.25,"rgb(0, 25, 255)"],\
[0.375,"rgb(0, 152, 255)"],[0.5,"rgb(44, 255, 150)"],[0.625,"rgb(151, 255, 0)"],\
[0.75,"rgb(255, 234, 0)"],[0.875,"rgb(255, 111, 0)"],[1,"rgb(255, 0, 0)"]

data = [Scattergeo(
       #locationmode = "USA-states",
        lon=lons,
        lat=lats,
        marker = dict(
            color = brights,
            #colorscale = scl,
            colorscale = 'YlGnBu',
            #reversescale = True,
            #opacity = 0.7,
            size = 10,
            colorbar = dict(
                titleside = "right",
                #outlinecolor = "rgba(68, 68, 68, 0)",
                #ticks = "outside",
                #showticksuffix = "last",
                #dtick = 0.1
                )
            )
    )]


my_layout = Layout(title="November 2019 Australia Fires",geo = dict(
            fitbounds="locations",            
            showland = True,
            landcolor = "rgb(250, 250, 250)",
            subunitcolor = "rgb(217, 217, 217)",
            countrycolor = "rgb(217, 217, 217)",
            countrywidth = 0.5,
            subunitwidth = 0.5
        ))
fig = {'data':data, 'layout':my_layout}


offline.plot(fig,filename='November 2019 Australia Fires.html')