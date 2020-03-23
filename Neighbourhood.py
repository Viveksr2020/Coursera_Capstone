import numpy as np # library to handle data in a vectorized manner
import time
import pandas as pd # library for data analsysis
from IPython.core.display import display
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
from bs4 import BeautifulSoup
from sklearn.cluster import KMeans 
import json # library to handle JSON files
import requests # library to handle requests
from pandas.io.json import json_normalize # tranform JSON file into a pandas dataframe

from geopy.geocoders import Nominatim # convert an address into latitude and longitude values

import folium # map rendering library
from IPython.display import HTML, display
from datetime import date
#Matplotlib and associated plotting modules
import matplotlib.cm as cm
import matplotlib.colors as colors
import matplotlib.pyplot as plt
import seaborn as sns
import googlemaps

from datetime import datetime

from googlemaps import Client

gmaps = googlemaps.Client(key='AIzaSyDdD-JCrFejxneJWEGj8JuNJpcGfANjB0w')


from sklearn.cluster import KMeans
 # @hidden_cell vivek
CLIENT_ID = '5IRXC0ZPHIPISLU52MO4HL5H5EGWZYT04FBEGTB0HQ45A5OS' # your Foursquare ID
CLIENT_SECRET = 'QXOB3XWMPKX3VSQTH2ZG1MQA2GYGHJ3HATGHBRZYAV5DMSO3' # your Foursquare Secret
VERSION = '20180605' # Foursquare API version
 
# # #@hidden_cell arnesh
# CLIENT_ID = '02LEF0GX5421KX3UOEVRXGDQTTBB3QP4H0ZFV5IZXOK1MLW2' # your Foursquare ID
# CLIENT_SECRET = 'CB4AXJLSIWIXBN0IVTDIV1RG0KXHYHGTUM3W02SVR3VUYOOR' # your Foursquare Secret
# VERSION = '20180605' # Foursquare API version
#   
#   
#   
# Pune Karve Road
address = 'Karve Road, Pune, India'
geolocator = Nominatim()
location = geolocator.geocode(address)
latitude = location.latitude
longitude = location.longitude
print('The geograpical coordinate of Karve Road Pune home are {}, {}.'.format(latitude, longitude))
  
neighborhood_latitude=18.5144052
neighborhood_longitude=73.8421049
LIMIT = 100 # limit of number of venues returned by Foursquare API
radius = 500 # define radius
#create URL
url = 'https://api.foursquare.com/v2/venues/explore?&client_id={}&client_secret={}&v={}&ll={},{}&radius={}&limit={}'.format(
    CLIENT_ID, 
    CLIENT_SECRET, 
    VERSION, 
    neighborhood_latitude, 
    neighborhood_longitude, 
    radius, 
    LIMIT)
#print(url) # display URL
results = requests.get(url).json()
  
def get_category_type(row):
    try:
        categories_list = row['categories']
    except:
        categories_list = row['venue.categories']
          
    if len(categories_list) == 0:
        return None
    else:
        return categories_list[0]['name']
      
venues = results['response']['groups'][0]['items']
SGnearby_venues = json_normalize(venues) # flatten JSON
#filter columns
filtered_columns = ['venue.name', 'venue.categories', 'venue.location.lat', 'venue.location.lng']
SGnearby_venues =SGnearby_venues.loc[:, filtered_columns]
#filter the category for each row
SGnearby_venues['venue.categories'] = SGnearby_venues.apply(get_category_type, axis=1)
#clean columns
SGnearby_venues.columns = [col.split(".")[-1] for col in SGnearby_venues.columns]
  
#print(SGnearby_venues.shape)
#display(SGnearby_venues.head(10))
  
#results display is hidden for report simplification 
latitude=18.5144052
longitude=73.8421049
#create map of Karve road place  using latitude and longitude values
map_sg = folium.Map(location=[latitude, longitude], zoom_start=18)
#add markers to map
for lat, lng, label in zip(SGnearby_venues['lat'], SGnearby_venues['lng'], SGnearby_venues['name']):
    label = folium.Popup(label, parse_html=True)
    folium.RegularPolygonMarker(
        [lat, lng],
        number_of_sides=30,
        radius=7,
        popup=label,
        color='blue',
        fill_color='#0f0f0f',
        fill_opacity=0.6,
    ).add_to(map_sg)  
      
map_sg.save("Karveroad.html")
  
results
  
  #print(soupstring) # Foursquare API version
#     
def foursquare_crawler (postal_code_list, neighborhood_list, lat_list, lng_list, LIMIT = 500, radius = 1000):
      result_ds = []
      counter = 0
      for postal_code, neighborhood, lat, lng in zip(postal_code_list, neighborhood_list, lat_list, lng_list):
             
          # create the API request URL
          url = 'https://api.foursquare.com/v2/venues/explore?&client_id={}&client_secret={}&v={}&ll={},{}&radius={}&limit={}'.format(
              CLIENT_ID, CLIENT_SECRET, VERSION, 
              lat, lng, radius, LIMIT)
                
          # make the GET request
          results = requests.get(url).json()["response"]['groups'][0]['items']
          print(results)
          tmp_dict = {}
          tmp_dict['Postal Code'] = postal_code; tmp_dict['Neighborhood(s)'] = neighborhood; 
          tmp_dict['Latitude'] = lat; tmp_dict['Longitude'] = lng;
          tmp_dict['Crawling_result'] = results;
          result_ds.append(tmp_dict)
          counter += 1
          print('{}.'.format(counter))
          print('Data is Obtained, for the Postal Code {} (and Neighborhoods {}) SUCCESSFULLY.'.format(postal_code, neighborhood))
      return result_ds;
     
    
DFSlough_Postcodes = pd.read_csv('/Users/arneshsrivastava/eclipse-workspace/combined_csv.csv')
  
Burnham_data = DFSlough_Postcodes[DFSlough_Postcodes['Locality_Name'] == 'Burnham']
#Burnham_data = Burnham_data.reset_index(drop=True).drop(columns = 'Unnamed: 0')
#print(Burnham_data.head())
  
  
    
Burnham_data.drop(['Admin_level3', 'Admin_level2', 'Admin_level1','country'], axis=1,inplace=True)
print(Burnham_data.head(20))
  
address_scar = 'Burnham, United Kingdom'
  
geolocator = Nominatim()
location = geolocator.geocode(address_scar)
latitude = location.latitude
longitude = location.longitude
  
print('The geograpical coordinate of "Burnham" are: {}, {}.'.format(latitude, longitude))
  
map_Burnham = folium.Map(location=[latitude, longitude], zoom_start=11.5)
  
 # add markers to map
for lat, lng, label in zip(Burnham_data['lat'], Burnham_data['longi'], Burnham_data['Route_Name']):
     label = folium.Popup(label, parse_html=True)
     folium.CircleMarker(
         [lat, lng],
         radius = 10,
         popup = label,
         color ='blue',
         fill = True,
         fill_color = '#3186cc',
         fill_opacity = 0.7).add_to(map_Burnham)  
       
map_Burnham.save("map_Burnham.html")
# 
print('Crawling different neighborhoods inside "Burnham"')
# Burnham_foursquare_dataset = foursquare_crawler(list(Burnham_data['address']),
#                                                    list(Burnham_data['Route_Name']),
#                                                    list(Burnham_data['lat']),
#                                                    list(Burnham_data['longi']),)
import pickle
# with open("Burnham_foursquare_dataset.txt", "wb") as fp:   #Pickling
#      pickle.dump(Burnham_foursquare_dataset, fp)
# print('Received Data from Internet is Saved to Computer')

with open("Burnham_foursquare_dataset.txt", "rb") as fp:   # Unpickling
     Burnham_foursquare_dataset = pickle.load(fp)

# This function is created to connect to the saved list which is the received database. It will extract each venue 
# for every neighborhood inside the database

def get_venue_dataset(foursquare_dataset):
    result_df = pd.DataFrame(columns = ['address', 'Route Name', 
                                           'Route Latitude', 'Route Longitude',
                                          'Venue', 'Venue Summary', 'Venue Category', 'Distance'])
    # print(result_df)
    
    for neigh_dict in foursquare_dataset:
        postal_code = neigh_dict['Postal Code']; neigh = neigh_dict['Neighborhood(s)']
        lat = neigh_dict['Latitude']; lng = neigh_dict['Longitude']
        print('Number of Venuse in Coordination "{}" Posal Code and "{}" Negihborhood(s) is:'.format(postal_code, neigh))
        print(len(neigh_dict['Crawling_result']))
        
        for venue_dict in neigh_dict['Crawling_result']:
            summary = venue_dict['reasons']['items'][0]['summary']
            name = venue_dict['venue']['name']
            dist = venue_dict['venue']['location']['distance']
            cat =  venue_dict['venue']['categories'][0]['name']
            
            result_df = result_df.append({'Address': postal_code, 'Route_Name': neigh, 
                              'Neighborhood Latitude': lat, 'Neighborhood Longitude':lng,
                              'Venue': name, 'Venue Summary': summary, 
                              'Venue Category': cat, 'Distance': dist}, ignore_index = True)
            # print(result_df)
    
    return(result_df)

Burnham_venues = get_venue_dataset(Burnham_foursquare_dataset)
print("Burnham_venues.head()")
print(Burnham_venues.head())
print(Burnham_venues.tail())
Burnham_venues.to_csv('Burnham_venues.csv')
Burnham_venues = pd.read_csv('Burnham_venues.csv')
neigh_list = list(Burnham_venues['Route_Name'].unique())
print('Number of Neighborhoods inside Burnham:')
print(len(neigh_list))
print('List of Neighborhoods inside Burnham:')
print(neigh_list)
neigh_venue_summary = Burnham_venues.groupby('Route_Name').count()
neigh_venue_summary.drop(columns = ['Unnamed: 0']).head()

print('There are {} uniques categories.'.format(len(Burnham_venues['Venue Category'].unique())))

print('Here is the list of different categories:')

list(Burnham_venues['Venue Category'].unique())
     
Burnham_onehot = pd.get_dummies(data = Burnham_venues, drop_first  = False, 
                              prefix = "", prefix_sep = "", columns = ['Venue Category'])
print(Burnham_onehot.head())


important_list_of_features =    Burnham_onehot.columns.values.tolist()
print("important list of feature before")
print(important_list_of_features)

####Grouping the Data by Neighborhoods
Burnham_onehot = Burnham_onehot[important_list_of_features].drop(
    columns = ['Unnamed: 0','Route Name','Route Latitude', 'Route Longitude','Neighborhood Latitude','Neighborhood Longitude','address','Address']).groupby(
    'Route_Name').sum()

print("final burnham_onhot")

print(Burnham_onehot.head())

from sklearn.cluster import KMeans

# run k-means clustering
kmeans = KMeans(n_clusters = 5, random_state = 0).fit(Burnham_onehot)

####Showing Centers of Each Cluster

means_df = pd.DataFrame(kmeans.cluster_centers_)
means_df.columns = Burnham_onehot.columns
means_df.index = ['G1','G2','G3','G4','G5']
means_df['Total Sum'] = means_df.sum(axis = 1)
means_df.sort_values(axis = 0, by = ['Total Sum'], ascending=False)
print(means_df.head())

#####Best Group is G5;
###Second Best Group is G1;
##Third Best Group is G4;
##Inserting "kmeans.labels_" into the Original Scarborough DataFrame

##Finding the Corresponding Group for Each Neighborhood.
neigh_summary = pd.DataFrame([Burnham_onehot.index, 1 + kmeans.labels_]).T
neigh_summary.columns = ['Neighborhood', 'Group']
print("neigh_summary")
print(neigh_summary)


print(neigh_summary[neigh_summary['Group'] == 5])
name_of_neigh = list(neigh_summary[neigh_summary['Group'] == 5]['Neighborhood'])[0]

# Merge two Dataframes on index of both the dataframes
mergedDf = neigh_summary.merge(Burnham_data, left_index=True, right_index=True)
print(mergedDf.head())

print("name_of_neigh")
print(name_of_neigh)
# Burnham_venues[Burnham_venues['Neighborhood'] == name_of_neigh].iloc[0,1:5].to_dict()
# 
# ####Second Best Neighborhoods
# print(neigh_summary[neigh_summary['Group'] == 1])
# 
# ###Third Best Neighborhood
# print(neigh_summary[neigh_summary['Group'] == 4])
# name_of_neigh = list(neigh_summary[neigh_summary['Group'] == 4]['Neighborhood'])[0]
# Burnham_venues[Burnham_venues['Neighborhood'] == name_of_neigh].iloc[0,1:5].to_dict()

#DFUKrailway_Station = pd.read_csv('ListofRailwayStation.csv')
filename= "slough_" + str(date.today())+ ".html"
map_slough = folium.Map(location=[51.50342695, -0.574872152385296])
  #folium.Map( location=[51.50342695, -0.574872152385296],zoom_start=13)
map_slough.save(filename)
  #print(DFSlough_Postcodes.head(20))
   
   
   
           
  #print(DFSlough_Postcodes.head(20))
map_slough = folium.Map(location = [51.50342695, -0.574872152385296], zoom_start = 10)
    
  #add neighborhood markers to the Toronto map
for lat, long, bor, neigh in zip(DFSlough_Postcodes['lat'], DFSlough_Postcodes['longi'], 
                                   DFSlough_Postcodes['Route_Name'], DFSlough_Postcodes['postal_town']):
      label = '{}, {}'.format(neigh, bor)
        
      label = folium.Popup(label, parse_html=True)
      folium.CircleMarker(
          [lat,long],
          radius = 7, 
          popup = label,
          color = 'red',
          fill = True,
          fill_color = 'white',
          fill_opacity = 0.7,
          parse_html = False).add_to(map_slough)
        
    
map_slough.save(filename)
   
   
list_Locality = DFSlough_Postcodes['Locality_Name'].unique()
  #print(list_Locality)
cleanedList = [x for x in list_Locality if str(x) != 'nan']
  #print(cleanedList)
   
def Locality_loc(list_of_places):
      for place in list_of_places:
          address = (place + ", United Kingdom")
          geolocator = Nominatim(user_agent="TO_explorer")
          location = geolocator.geocode(address)
          latitude = location.latitude
          longitude = location.longitude
          print('{''}, {}, {},'.format(place,latitude,longitude))
   
  #Locality_loc(cleanedList)
 
import numpy as np
   
boroughs = ['Slough', 51.50342695, -0.5748721523852964,
  'Berkshire', 51.453488899999996, -1.0318729593399247,
  'Burnham', 51.5233926, -0.6470844,
  'Farnham Royal', 51.5374195, -0.6173339,
  'Taplow', 51.5233325, -0.6818864,
  'Datchet', 51.4838483, -0.5784291,
  'Dorney', 51.5028664, -0.6607042]
   
boroughs_df = pd.DataFrame(np.array(boroughs).reshape(7,3), columns = ["Locality_Name","Latitude","Longitude"])
   
  #print(boroughs_df)
   
  # The geographical coordinates for Downtown Toronto
DT_lat = boroughs_df.iloc[1,1]
DT_long = boroughs_df.iloc[1,2]
   
  # The dataframe that contains all the Downtown Toronto neighborhoods
DT_df = DFSlough_Postcodes[DFSlough_Postcodes['Locality_Name'] == 'Slough'].reset_index(drop = True)
  #print(DT_df)
   
  # create map of Downtown Toronto neighborhoods using latitude and longitude values
map_DT = folium.Map(location=[DT_lat, DT_long], zoom_start=10)
   
  # add markers to map
for lat, lng, label in zip(DT_df['lat'], DT_df['longi'], DT_df['Route_Name']):
      label = folium.Popup(label, parse_html=True)
      folium.CircleMarker(
          [lat, lng],
          radius=5,
          popup=label,
          color='red',
          fill=True,
          fill_color='white',
          fill_opacity=0.7,
          parse_html=False).add_to(map_DT)  
   
DFSlough = DFSlough_Postcodes[['lat', 'longi']].copy()
  #print(DFSlough)
   
   
   
kmeans = KMeans(n_clusters=3).fit(DFSlough)
centroids = kmeans.cluster_centers_
print(centroids)
plt.scatter(DFSlough['lat'], DFSlough['longi'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
plt.show()
k=3
  
   
def get_venue_dataset(foursquare_dataset):
      result_df = pd.DataFrame(columns = ['Postal Code', 'Neighborhood', 
                                             'Neighborhood Latitude', 'Neighborhood Longitude',
                                            'Venue', 'Venue Summary', 'Venue Category', 'Distance'])
      # print(result_df)
       
      for neigh_dict in foursquare_dataset:
          postal_code = neigh_dict['Postal Code']; neigh = neigh_dict['Neighborhood(s)']
          lat = neigh_dict['Latitude']; lng = neigh_dict['Longitude']
          print('Number of Venuse in Coordination "{}" Posal Code and "{}" Negihborhood(s) is:'.format(postal_code, neigh))
          print(len(neigh_dict['Crawling_result']))
           
          for venue_dict in neigh_dict['Crawling_result']:
              summary = venue_dict['reasons']['items'][0]['summary']
              name = venue_dict['venue']['name']
              dist = venue_dict['venue']['location']['distance']
              cat =  venue_dict['venue']['categories'][0]['name']
               
               
              # print({'Postal Code': postal_code, 'Neighborhood': neigh, 
              #                   'Neighborhood Latitude': lat, 'Neighborhood Longitude':lng,
              #                   'Venue': name, 'Venue Summary': summary, 
              #                   'Venue Category': cat, 'Distance': dist})
               
              result_df = result_df.append({'Postal Code': postal_code, 'Neighborhood': neigh, 
                                'Neighborhood Latitude': lat, 'Neighborhood Longitude':lng,
                                'Venue': name, 'Venue Summary': summary, 
                                'Venue Category': cat, 'Distance': dist}, ignore_index = True)
              # print(result_df)
       
      return(result_df)
   
   
  # scarborough_venues = get_venue_dataset(Scarborough_foursquare_dataset)
  # print(scarborough_venues.head())
  # print(scarborough_venues.tail())
  # scarborough_venues.to_csv('scarborough_venues.csv')
   
scarborough_venues = pd.read_csv('scarborough_venues.csv')
   
neigh_list = list(scarborough_venues['Neighborhood'].unique())
# print('Number of Neighborhoods inside Scarborough:')
  # print(len(neigh_list))
  # print('List of Neighborhoods inside Scarborough:')
  # print(neigh_list)
neigh_venue_summary = scarborough_venues.groupby('Neighborhood').count()
  #print(neigh_venue_summary.drop(columns = ['Unnamed: 0']).head())
   
  #print('There are {} uniques categories.'.format(len(scarborough_venues['Venue Category'].unique())))
   
  #print('Here is the list of different categories:')
list(scarborough_venues['Venue Category'].unique())
   
scarborough_onehot = pd.get_dummies(data = scarborough_venues, drop_first  = False, 
                                prefix = "", prefix_sep = "", columns = ['Venue Category'])
  #print(scarborough_onehot.head())
   
scarborough_onehot = scarborough_onehot.drop(
      columns = ['Neighborhood Latitude', 'Neighborhood Longitude']).groupby(
      'Neighborhood').sum()
   
   
  #print(scarborough_onehot.head())
   
feat_name_list = list(scarborough_onehot.columns)
restaurant_list = []
   
   
for counter, value in enumerate(feat_name_list):
      if value.find('Restaurant') != (-1):
          restaurant_list.append(value)
           
scarborough_onehot['Total Restaurants'] = scarborough_onehot[restaurant_list].sum(axis = 1)
scarborough_onehot = scarborough_onehot.drop(columns = restaurant_list)
   
   
feat_name_list = list(scarborough_onehot.columns)
joint_list = []
   
   
for counter, value in enumerate(feat_name_list):
      if value.find('Joint') != (-1):
          joint_list.append(value)
           
scarborough_onehot['Total Joints'] = scarborough_onehot[joint_list].sum(axis = 1)
scarborough_onehot = scarborough_onehot.drop(columns = joint_list)
   
  #print(scarborough_onehot)
   
  # import k-means from clustering stage
from sklearn.cluster import KMeans
   
  # run k-means clustering
kmeans = KMeans(n_clusters = 5, random_state = 0).fit(scarborough_onehot)
   
means_df = pd.DataFrame(kmeans.cluster_centers_)
means_df.columns = scarborough_onehot.columns
means_df.index = ['G1','G2','G3','G4','G5']
means_df['Total Sum'] = means_df.sum(axis = 1)
means_df.sort_values(axis = 0, by = ['Total Sum'], ascending=False)
 
  
# scarborough_venues = get_venue_dataset(Scarborough_foursquare_dataset)
# neigh_summary = pd.DataFrame([scar_ds.index, 1 + kmeans.labels_]).T
# neigh_summary.columns = ['Neighborhood', 'Group']
# print(neigh_summary)
  
DFSlough_Rent = pd.read_csv('/Users/arneshsrivastava/eclipse-workspace/ListofRentalProperty.csv')
print(DFSlough_Rent.head())
map_slough = folium.Map(location = [51.50342695, -0.574872152385296], zoom_start = 10)
#   1 bedroom mark it green
#   2 bedroom mark it yellow
#   3> bedroom mark purple
#  
for lat, long, bor, neigh,nofbeds in zip(DFSlough_Rent['latitude'], DFSlough_Rent['latitude'], 
                                   DFSlough_Rent['Address'], DFSlough_Rent['Rent'],DFSlough_Rent['No_oF_Bedrooms']):
      label = '{}, {}'.format(neigh, bor)
for  i in range(1,len(DFSlough_Rent)):  
     label = folium.Popup(label, parse_html=True)
      
     numberofrooms= DFSlough_Rent['No_oF_Bedrooms'][i]
     print("lat :"+ str(DFSlough_Rent['latitude'][i]))
     print("longi:" + str(DFSlough_Rent['longitude'][i]))
     print("Address:" + str(DFSlough_Rent['Address'][i]))
     print("numberofrooms"+ str(numberofrooms))
     if int(numberofrooms) == 1:
        folium.CircleMarker([DFSlough_Rent['latitude'][i],DFSlough_Rent['longitude'][i]],
                         radius= 4,
                         color='green',
                         tooltip=DFSlough_Rent['Address'][i]+ ":" + str(numberofrooms),
                         fill=True).add_to(map_slough)
  
     else:
        if  int(numberofrooms) == 2:   
            folium.CircleMarker([DFSlough_Rent['latitude'][i],DFSlough_Rent['longitude'][i]],
                         radius= 7,
                         color='purple',
                         tooltip=DFSlough_Rent['Address'][i]+ ":" + str(numberofrooms),
                         fill=True).add_to(map_slough)
        else:
            folium.CircleMarker([DFSlough_Rent['latitude'][i],DFSlough_Rent['longitude'][i]],
                         radius= 10,
                         color='red',
                         tooltip=DFSlough_Rent['Address'][i]+ ":" + str(numberofrooms),
                         fill=True).add_to(map_slough)
  
  
     print(filename)
     map_slough.save(filename)
  #print(DFSlough_Postcodes.head(20))
 
                 
DFSlough_Rail = pd.read_csv('/Users/arneshsrivastava/eclipse-workspace/ListofRailwayStation.csv')
 
station =['Slough','Windsor & Eton Riverside','indsor and Eton Central','Datchet','Langley','Burnham','Taplow','Iver','Sunnymeads','Wraysbury']
 
for i in range(len(station)):
       
      geocode_result = gmaps.geocode(station[i].strip()+','+ 'United Kingdom')
      lati = geocode_result[0]['geometry']['location']['lat']
      longi = geocode_result[0]['geometry']['location']['lng']
      station1 = station[i]
      icon_url = 'https://cdn1.iconfinder.com/data/icons/maps-locations-2/96/Geo2-Number-512.png'
      icon = folium.features.CustomIcon(icon_url,icon_size=(28, 30))  # Creating a custom Icon
   
   
      folium.Marker(location=[lati, longi], tooltip=station1, icon=icon).add_to(map_slough)  #adding it to the map
    
map_slough.save(filename)
  # #print(DFSlough_Postcodes.head(20))
   
URL= "https://en.wikipedia.org/wiki/List_of_schools_in_Slough"
   
   
  # icon_path2 = "https://thenounproject.com/search/?q=railway%20station&i=2426228"
  # icon2 = folium.features.CustomIcon(icon_image=icon_path2 ,icon_size=(50,50))
   
data=[]
school =''
   
page = requests.get(URL)
#print(page.content)
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)
#print(soupstring)
 
soupstring = soup.find_all('li')
   
for i in range(10,45): 
      school= soupstring[i].text
      school = school.replace("'", '')
      school = school.replace("-", '')
      geocode_result = gmaps.geocode(school+','+ 'United Kingdom')
      latii = geocode_result[0]['geometry']['location']['lat'] 
      longii = geocode_result[0]['geometry']['location']['lng'] 
      print(school + " ::::"+ str(latii) +"::::" + str(longii))
    
      folium.Marker([latii, longii],
                            tooltip=school,
                            popup= school,
                            icon=folium.Icon(color='blue', icon='leaf')).add_to(map_slough)
  #     folium.Marker(location=[lati, longi],icon=icon2).add_to(map_slough) 
       
 
      legend_html = '''
                    <div style="position: fixed; 
                                bottom: 50px; left: 50px; width: 200px; height: 170px; 
                                border:2px solid grey; z-index:9999; font-size:14px;
                                ">&nbsp; Color Legend <br>
                                  &nbsp; Schools  &nbsp; <i class="fa fa-map-marker fa-2x" style="color:blue"></i><br>
                                  &nbsp; 1 BHK  &nbsp; <i class="fa fa fa-circle fa-.2x" style="color:green"></i><br>
                                  &nbsp; 2 BHK  &nbsp; <i class="fa ffa fa-circle-o fa-1x" style="color:purple"></i><br>
                                  &nbsp; 3-4-5 BHK  &nbsp; <i class="fa ffa fa-circle-o fa-1.75x" style="color:red"></i><br>
                                  &nbsp; Railway station &nbsp; <i class="fa fa-map-marker fa-2x" style="color:black"></i>
                    </div>
                    ''' 
     
map_slough.get_root().html.add_child(folium.Element(legend_html))
map_slough.save(filename)
