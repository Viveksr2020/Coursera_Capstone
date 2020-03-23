import numpy as np # library to handle data in a vectorized manner

import pandas as pd # library for data analsysis


import json # library to handle JSON files

#!conda install -c conda-forge geopy --yes # uncomment this line if you haven't completed the Foursquare API lab

from geopy.geocoders import Nominatim # convert an address into latitude and longitude values

import requests # library to handle requests

from pandas.io.json import json_normalize # tranform JSON file into a pandas dataframe

# Matplotlib and associated plotting modules

import matplotlib.cm as cm

import matplotlib.colors as colors

# import k-means from clustering stage

from sklearn.cluster import KMeans


import folium # map rendering library

from bs4 import BeautifulSoup

import lxml

print('Libraries imported.')

####################################

from bs4 import BeautifulSoup

import googlemaps

import pprint

import time

##from GoogleMAPsAPIKey import get_api_key
import geopandas as geoo

import numpy as np

import pandas as pd

from shapely.geometry import Point

import folium 
from datetime import date
import missingno as msn

import seaborn as sns

import matplotlib.pyplot as plt

#import rhinoscriptsytnax as rs 
import os

import requests

import pandas as pand

from geopy.exc import GeocoderTimedOut

##API_KEY = get_api_key()

##gmaps=googlemap.client(key=API_KEY)

import googlemaps

from datetime import datetime

from googlemaps import Client

gmaps = googlemaps.Client(key='xxxxxx')

column_names = ['Postalcode', 'Latitude', 'Longitude']


 

dfListofPostCodes = {}

PostCodeArray =[]

#URL= "https://www.cambridge-news.co.uk/news/uk-world-news/coronavirus-cases-england-county-region-17901168"
#URL ="https://checkmypostcode.uk/slough/slough#.XlfgqC2cZbV"
#url2 ="https://checkmypostcode.uk/slough/colnbrook#.XnOYVpP7RQI"
#url3="https://checkmypostcode.uk/slough/dorney#.XnOZDJP7RQI"
#url4="https://checkmypostcode.uk/slough/myrke#.XnOZf5P7RQI"
#url5="https://checkmypostcode.uk/slough/poyle#.XnOZl5P7RQI"
# url6="https://checkmypostcode.uk/slough/slough#.XnOZp5P7RQI"
#url7="https://checkmypostcode.uk/slough/stoke-poges#.XnOZyJP7RQI"
url8="https://checkmypostcode.uk/slough/rural#.XnOZ35P7RQI"

page = requests.get(url8)

soup = BeautifulSoup(page.content, 'html.parser')
soupstring = soup.find(class_="threecol")
# @hidden_cell 
CLIENT_ID = '' # your Foursquare ID
CLIENT_SECRET = '' # your Foursquare Secret
VERSION = '20180605' # Foursquare API version


#print(soupstring)
Locality_Name=''

postal_town=''

Admin_level1=''

Admin_level2=''
Admin_level3=''

postal_code=''
Route_Name=''
lati=''
longi=''
NumofPatient=''
address=''

#country = pd.read_csv('/Users/arneshsrivastava/eclipse-workspace/ListofCoronoCases.csv')



StrScriptAll = soupstring.find_all("a")

print(len(StrScriptAll))

 

with open('ListofPostcodes1810.csv', 'w') as writefile:
  
     writefile.write('address' + ',' + 'lat' + ',' + 'longi' + ',' +
  
                           'Route_Name' + ','  + 'Locality_Name' + ',' + 'postal_town' + ','+
  
                           'Admin_level3' + ','  + 'Admin_level2' + ',' + 'Admin_level1' + ','+ 'country')
  
     writefile.write("\n")                     ### this is next line character so write in next line

    
     for list in range(0,93):   ### this provides list like [a, b, c...]
 
           jsonData  = StrScriptAll[list] ### this picks up the first <a href="/sl09rr">SL0 9RR Market Lane</a>,
 
           dataText1 = jsonData.get_text(separator=" ")### this picks up the value of SL0 9RR Market Lane
 
           address = dataText1  ### assign the value to address

            
           geocode_result = gmaps.geocode(address.strip() +',' +'United Kingdom')
           lati = geocode_result[0]['geometry']['location']['lat']
           longi = geocode_result[0]['geometry']['location']['lng']
           address = address.replace(',', '', 1)
            
           #print(address)
           for i in range(len(geocode_result[0]['address_components'])):
                     if (geocode_result[0]['address_components'][i]['types'][0] == "route"):
 
                         Route_Name = geocode_result[0]['address_components'][i]['long_name']
                     else:
                         if (geocode_result[0]['address_components'][i]['types'][0][1] == "sublocality"):
                            Locality_Name = geocode_result[0]['address_components'][i]['long_name']
                                                    
                         else:
                             if (geocode_result[0]['address_components'][i]['types'][0] == "locality"): 
                                Locality_Name = geocode_result[0]['address_components'][i]['long_name']
                             else:
                                 if  (geocode_result[0]['address_components'][i]['types'][0] == "postal_town"): 
 
                                     postal_town = geocode_result[0]['address_components'][i]['long_name']
                                 else:
                                     if (geocode_result[0]['address_components'][i]['types'][0] == "administrative_area_level_3"):
 
                                         Admin_level3 = geocode_result[0]['address_components'][i]['long_name']
 
                                         Admin_level3 = Admin_level3.replace(',', '', 1)
                                     else:
                                         if  (geocode_result[0]['address_components'][i]['types'][0] == "administrative_area_level_2"): 
                                              Admin_level2 = geocode_result[0]['address_components'][i]['long_name']         
                                         else:
                                            if  (geocode_result[0]['address_components'][i]['types'][0] == "administrative_area_level_1"): 
                                                 Admin_level1 = geocode_result[0]['address_components'][i]['long_name']
                                            else:
                                                if (geocode_result[0]['address_components'][i]['types'][0] == "country"):
                                                    country = geocode_result[0]['address_components'][i]['long_name'] 
                                                
                                                   
           url = 'https://api.foursquare.com/v2/venues/search?client_id={}&client_secret={}&ll={},{}&v={}&radius={}&limit={}'.format(
                CLIENT_ID, 
                CLIENT_SECRET, 
                lati, 
                longi, 
                VERSION, 
                1500, 
                50)
            
        # make the GET request
           print(requests.get(url))
           print(requests.get(url).json())
           print(requests.get(url).json()["response"]['groups'][0]['items'])
           
           print(address + ',' + str(lati) + ',' + str(longi) + ',' + Route_Name + ','  + str(Locality_Name) + ',' + postal_town + ','+
                            Admin_level3 + ','  + Admin_level2 + ',' + Admin_level1 + ','+ country)
           writefile.write(address + ',' + str(lati) + ',' + str(longi) + ',' + Route_Name + ','  + str(Locality_Name) + ',' + postal_town + ','+
                            Admin_level3 + ','  + Admin_level2 + ',' + Admin_level1 + ','+ country)
           writefile.write("\n")                     ### this is next line character so write in next line
 
 

