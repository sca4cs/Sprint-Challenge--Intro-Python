# Create a class to hold a city location. Call the class "City". It should have
# fields for name, latitude, and longitude.

class City:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# Use Python's built-in "csv" module to read this file so that each record is
# imported into a City instance. (You're free to add more attributes to the City
# class if you wish, but this is not necessary.) Google "python 3 csv" for
# references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.

cities = []

import csv
with open('cities.csv') as csvfile:
    citiesreader = csv.reader(csvfile)
    for i, row in enumerate(citiesreader):
        if i != 0:
            cities.append(City(row[0], row[3], row[4]))

# Print the list of cities (name, lat, lon), 1 record per line.

for c in cities:
    print(f"\nName: {c.name}, Latitude: {c.latitude}, Longitude: {c.longitude}")

# *** STRETCH GOAL! ***
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Output the cities that fall
# within this square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other (what is latMin, latMax?)
# then search for cities.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

latLon1 = input("Enter lat1, lon1: ")
latLon2 = input("Enter lat2, lon2: ")
latLon1 = latLon1.replace(" ", "").split(',')
latLon2 = latLon2.replace(" ", "").split(',')

lat1 = 0
lat2 = 0
lon1 = 0
lon2 = 0

if int(latLon1[0]) > int(latLon2[0]):
    lat1 = int(latLon2[0])
    lat2 = int(latLon1[0])
else:
    lat1 = int(latLon1[0])
    lat2 = int(latLon2[0])

if int(latLon1[1]) > int(latLon2[1]):
    lon1 = int(latLon2[1])
    lon2 = int(latLon1[1])
else:
    lon1 = int(latLon1[1])
    lon2 = int(latLon2[1])

for c in cities:
    if  float(c.latitude) >= lat1 and float(c.latitude) <= lat2 and float(c.longitude) >= lon1 and float(c.longitude) <= lon2:
        print(f"{c.name}: {( c.latitude,c.longitude)}")