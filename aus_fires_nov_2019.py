# Josh Jacobsen - MW 2:30pm
# JSON_Project

# - - - - Australian Fires - November 2019 - - - - 

import plotly
import json
import csv
from plotly.graph_objs import Scattergeo,Layout
from plotly import offline

#Open Fires Data File and Read
file_2019_fires = open('MODIS_C6_Australia_NewZealand_MCD14DL_NRT_2019331.txt','r')
data_2019_fires = csv.reader(file_2019_fires,delimiter=',')

#Get Row of Headers
header_row = next(data_2019_fires)

#Print Header Data Type
#print(type(header_row))

#Loop Through Columns and Print Index and Name
#for index,column_header in enumerate(header_row):
#   print(index,column_header)

#Create Lists for Fire Brightness, Longitudes, and Ladatudes
brights = []
lons = []
lats = []
for row in data_2019_fires:
    lats.append(row[0])
    lons.append(row[1])
    brights.append(int(float(row[2]))) #for some reason doing just int() didn't work

#Print Values of First 10 in Each List
#print(brights[:10])
#print(lons[:10])
#print(lats[:10])

#Load Data to Create Plot of Fire Data
data = [Scattergeo(
        lon=lons,
        lat=lats,
        #Customize Markers
        marker = dict(
            color = brights,
            colorscale = 'Viridis',
            reversescale = True,
            line=dict(width=1,color='White'),
            size = 12,
            #Customize Colorbar
            colorbar = dict(
                titleside = "top",
                title='Brightness'
                )
            )
    )]

#Create/Customize Plot Layout
my_layout = Layout(title="Australian Fires - November 2019",
            geo = dict(
                fitbounds="locations",            
                showland = True,
                landcolor = "rgb(229, 236, 246)",
                )
            )

#Generate Figure from Data and Layout
fig = {'data':data, 'layout':my_layout}

#Plot Figure in Offline Mode and Save HTML File
offline.plot(fig,filename='Australian Fires - November 2019.html')