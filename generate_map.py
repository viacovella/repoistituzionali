# preamble
# this is based on the https://www.youtube.com/watch?v=SgacOaHoJLs tutorial
# by Dario Festa - July 17, 2020

# folium is the library we are going to use to visualize our resuls on a map
import folium

# other relevant libraries
import numpy as np
import pandas as pd

# Import data from the gsheet
# this is based on https://towardsdatascience.com/read-data-from-google-sheets-into-pandas-without-the-google-sheets-api-5c468536550

sheet_id = "1zXCtxu0d0vwH6VSpn-wotc_zSF6c42LoOWJhC3pXewg"
sheet_name = "AteneiStatali"
# https://docs.google.com/spreadsheets/d/1zXCtxu0d0vwH6VSpn-wotc_zSF6c42LoOWJhC3pXewg/edit?pli=1#gid=0
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"


adataframe = pd.read_csv('https://docs.google.com/spreadsheets/d/' + 
                   sheet_id +
                   '/export?gid=0&format=csv',
                   header=0,
                   index_col=None
                  )

print(adataframe)



# create the basemap
# coordinates are located near Rome
# zoom_start level reflects the depth of the starting image (greater numbers relate to deeper zoom)
# tiles refers to what kind of background map are we going to visualize
theMap = folium.Map(location = [43,12], zoom_start = 6, tiles = "CartoDB positron")

# # Place a marker
for p in np.arange(61):
    folium.Marker(
        location=[float(adataframe.loc[p,'Lat']),float(adataframe.loc[p,'Long'])],
        popup=adataframe.loc[p, 'Nome'],
        tooltip=adataframe.loc[p, 'Denominazione'],
        icon=folium.Icon(color=adataframe.loc[p, 'color'],
                         icon=adataframe.loc[p, 'symbol'],
                         prefix='fa')
                ).add_to(theMap)

# theMap
# this saves the final result on an interactive html file
theMap.save("prova.html")