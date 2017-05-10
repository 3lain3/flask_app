import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from geopy.geocoders import Nominatim

from googleplaces import GooglePlaces, types, lang
YOUR_API_KEY =os.environ.get("GOOGLE_API_KEY")
google_places = GooglePlaces(YOUR_API_KEY)

######################- Origninal module commands from Google Places API -###########################

# query_result = google_places.nearby_search(
#         location='Bay Parkway, Brooklyn', keyword='food',
#         radius=2000, types=[types.TYPE_FOOD])

# for place in query_result.places:
# 	print(place.name)

#################################- Look up food as a function -######################################

def search_food(address):
	geolocator = Nominatim()
	location = geolocator.geocode(address)
	query_result = google_places.nearby_search(
		location = location,
		keyword = 'food',
		radius = 150,
		types = [types.TYPE_FOOD])

	restaurants = []
	for place in query_result.places:
		restaurants.append(place.name)
	return restaurants
	