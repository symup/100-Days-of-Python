DICTIONARY IN LIST

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country_visited,time_visited,cities_visited):
    #Creating new dictionary
    new_country = {}
    # Add each of these pieces of data into dict
    new_country["country"] = country_visited
    new_country["visits"] = time_visited
    new_country["cities"] = cities_visited
    #Take travel_log, using append() to add the list
    travel_log.append(new_country)

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)


OUTPUT:
  
'''
[
{'country': 'France', 'visits': 12, 'cities': ['Paris', 'Lille', 'Dijon']},
{'country': 'Germany', 'visits': 5, 'cities': ['Berlin', 'Hamburg', 'Stuttgart']},
{'country': 'Russia', 'visits': 2, 'cities': ['Moscow', 'Saint Petersburg']}
]
'''
