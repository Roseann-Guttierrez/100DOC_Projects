# learning to use APIs
# Using Open Notify API to get info on astronauts in the space station

# Import requests module
import requests

# create variable for URL that will be used
url = 'http://api.open-notify.org/astros.json'

# Use a GET request to retrieve data from URL
people = requests.get (url)

# Use JSON decode module to convert results to JSON
people_json = people.json()

# To print dictionary to screen
print (people_json)

#To print the number of people in space
print("Number of people in space:",people_json['number'])

#To print the names of people in space using a for loop
for p in people_json['people']:
    print(p['name'])