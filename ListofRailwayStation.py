from bs4 import BeautifulSoup
import requests
import pandas as pandu
import json
from shapely.ops import substring
#from IPython.display import display_html


Str1=''
station =['Slough','Windsor & Eton Riverside','indsor and Eton Central','Datchet','Langley','Burnham','Taplow','Iver','Sunnymeads','Wraysbury']
#urlwiki1 = "https://www.doogal.co.uk/london_stations.php"
urlwiki2="https://www.google.com/search?rlz=1C5CHFA_enGB881GB881&sxsrf=ALeKk02JLiX4x4oQF9efhfShXETvFWH1jQ:1584879375737&q=list+of+railway+station+near+slough?&npsic=0&rflfq=1&rlha=0&rllag=51497537,-600614,1717&tbm=lcl&ved=2ahUKEwiblM_hh67oAhVuUxUIHfxzDdMQjGp6BAgLEBw&tbs=lrf:,lf:1,lf_ui:8&rldoc=1"
valid_headers = ['Station', 'Zone', 'PostCode', 'Latitude','Longitude']
page = requests.get(urlwiki2)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup)
soupstring = soup.find_all('script')


print(soupstring)
data_tables = soup.table


Station=[]
Zone=[]
PostCode=[]
Latitude=[]
Longitude=[]


#print("number of tables"+ str(len(data_tables)))


data = []
#print(data_tables)

with open('ListofRailwayStation.csv', 'w') as writefile:
          writefile.write('Station' + ',' + 'Zone' + ',' + 'PostCode' + ','
                             +'Latitude' + ',' + 'Longitude' 
                             )
          writefile.write("\n")
          

 
          rows = data_tables.find_all('tr')

          for row in rows:
              cols = row.find_all('td')
              cols = [ele.text.strip() for ele in cols]
              data.append([ele for ele in cols if ele])
    
      #print("number of rows" + str(len(data)))
          #print(data)
          for x in range(1,len(data)):
    
              print("x"+ str(x))
              Station= data[x][0].replace(',','')
              print("Station:" + Station)
              
              Zone= data[x][1].replace(',','')
              print("Zone:" + Zone)
              
              PostCode= data[x][2]
              print("PostCode:" + PostCode)
            
              Latitude= data[x][3]
              print("Latitude:" + Latitude)
              
              Longitude= data[x][4]
              print("Longitude:" + Longitude)
                    
              writefile.write(Station + ',' + str(Zone) +','+ str(PostCode) + ','+ str(Latitude) +',' + str(Longitude))
              
              writefile.write("\n")
                        
