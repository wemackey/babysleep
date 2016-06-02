# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 04:43:58 2016

@author: wayne
"""
import numpy as np
import pandas as pd
from geoip import geolite2
import matplotlib
import plotly.plotly as py
import gmplot
matplotlib.style.use('ggplot')

inFile = "/Users/wayne/babysleep/webform_views_register_your_baby_for_the_research_study20160424000000.csv"
# load csv
hdr = (['sID', 'uID', 'instructions', 'instructions1', 'instructions2','instructions3', 'email', 
        'kID','instructionsKid','DOB','gender','firstName','middleInitial','instructions4',
        'instructions5','instructions6','timeStamp','ip'])
register_info_data = pd.read_csv(inFile, header=0, names=hdr, error_bad_lines=False)

# Now let's trim useless columns and create tables
register_info_table = register_info_data.drop('instructions',axis=1)
register_info_table = register_info_table.drop('instructions1',axis=1)
register_info_table = register_info_table.drop('instructions2',axis=1)
register_info_table = register_info_table.drop('instructions3',axis=1)
register_info_table = register_info_table.drop('instructions4',axis=1)
register_info_table = register_info_table.drop('instructions5',axis=1)
register_info_table = register_info_table.drop('instructions6',axis=1)
register_info_table = register_info_table.replace({"''":np.nan},regex=True)
register_info_table = register_info_table.replace({"'":""},regex=True)

ip_list = register_info_table['ip']
geo_dict = []
pair = []
lon = []
lat = []

for x in range(len(ip_list)):
    match = geolite2.lookup(ip_list[x])
    if match is not None:
        geo_dict.append(match.to_dict())
        pair.append(match.location)
        lat.append(match.location[0])
        lon.append(match.location[1])
        
lon = pd.Series(lon)
lat = pd.Series(lat)
pair = pd.Series(pair)

gmap = gmplot.GoogleMapPlotter(37.428, -122.145, 1)

#gmap.plot(lat, lon, 'cornflowerblue', edge_width=10)
#gmap.scatter(lat, lon, '#3B0B39', size=400, marker=True)
#gmap.scatter(lat, lon, 'k', marker=True)
#gmap.heatmap(lat, lon, threshold=1, radius=40)

gmap.draw("mymap.html")

# Now let's make our plot

cities = []

city = dict(
    type = 'scattergeo',
    locationmode = 'USA-states',
    lon = lon,
    lat = lat,
    marker = dict(
        size = 10,
        color = 'rgb(0,116,217)',
        line = dict(width=0.5, color='rgb(40,40,40)'),
        sizemode = 'area'
    ))
cities.append(city)

layout = dict(
        title = 'Babysleep study participant locations<br>(Click legend to toggle traces)',
        showlegend = True,
        geo = dict(
            scope='usa',
            projection=dict( type='albers usa' ),
            showland = True,
            landcolor = 'rgb(217, 217, 217)',
            subunitwidth=1,
            countrywidth=1,
            subunitcolor="rgb(255, 255, 255)",
            countrycolor="rgb(255, 255, 255)"
        ),
    )

fig = dict( data=cities, layout=layout )
url = py.plot( fig, validate=False, filename='d3-bubble-map-populations' )