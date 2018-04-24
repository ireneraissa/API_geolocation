from geopy.geocoders import Nominatim
import pandas as pd
from geopy.distance import great_circle
import googlemaps

from gmplot import gmplot


pharmacie=pd.read_csv("pharmacies.csv", names=['names','longitude','latitude', 'url', 'number', 'count'])
pharmacie.index=range(len(pharmacie))
maposition=(41.49008, -71.312796)
distance_position=[]
for (i,j) in list(zip(pharmacie.longitude, pharmacie.latitude)):
    lon_lat=(i,j)
    distance_position.append(great_circle(lon_lat, maposition).miles)
    
index_plus_proche=distance_position.index(min(distance_position))
pharmacie.ix[index_plus_proche]
