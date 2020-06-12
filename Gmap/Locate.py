from googleplaces import GooglePlaces, types, lang 
import requests 
import json 
from Geo_Location_finder import *
  

API_KEY='AIzaSyBeQ8EMs01Cnt9IHZXwqzUQOVqwra-WPJk'
  
# Initialising the GooglePlaces constructor 
google_places = GooglePlaces(API_KEY) 
list1=GetUserGeoLocation()
# call the function nearby search with 
# the parameters as longitude, latitude, 
# radius and type of place which needs to be searched of  
# type HOSPITAL
query_result = google_places.nearby_search(  
        lat_lng ={'lat': list1[0], 'lng': list1[1]}, 
        radius = 1000,  
        types =[types.TYPE_HOSPITAL]) 
  
# If any attributions related  
# with search results print them 
if query_result.has_attributions: 
    print (query_result.html_attributions) 
  
  
for place in query_result.places: 
    print (place.name) 
    print("Latitude", place.geo_location['lat']) 
    print("Longitude", place.geo_location['lng']) 
    print() 