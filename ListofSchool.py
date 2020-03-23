
import numpy as np # library to handle data in a vectorized manner

import pandas as pd # library for data analsysis


pd.set_option('display.max_columns', None)

pd.set_option('display.max_rows', None)

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

#from sklearn.datasets.samples_generator import make_blobs

#!conda install -c conda-forge folium=0.5.0 --yes # uncomment this line if you haven't completed the Foursquare API lab

import folium # map rendering library

from bs4 import BeautifulSoup

import lxml

print('Libraries imported.')

###############################
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

gmaps = googlemaps.Client(key='AIzaSyDdD-JCrFejxneJWEGj8JuNJpcGfANjB0w')

 
dfListofPostCodes = {}

PostCodeArray =[]

URL= "https://en.wikipedia.org/wiki/List_of_schools_in_Slough"

data=[]
school =''

page = requests.get(URL)
#print(page.content)
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)
soupstring = soup.find(class_="mw-parser-output")
#print(soupstring)
soupstring = soupstring.find_all('li')

for i in range(10,28): 
    School= soupstring[i].text
    school = school.replace("'", '')
    school = school.replace("-", '')
    geocode_result = gmaps.geocode(School+','+ 'United Kingdom')
    lati = geocode_result[0]['geometry']['location']['lat'] 
    longi = geocode_result[0]['geometry']['location']['lng'] 
    print(School + " ::::"+ str(lati) +"::::" + str(longi))
 