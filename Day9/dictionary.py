programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    123: "This is a number as a key, which is also valid in Python dictionaries."
}

print(programming_dictionary["Bug"])    
print(programming_dictionary["Function"])
print(programming_dictionary[123])
# Adding new items to the dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary["Loop"])
# Create an empty dictionary
empty_dictionary = {}     

#looping through a dictionary
for key in programming_dictionary:
    print(key)          # prints the keys of the dictionary
    print(programming_dictionary[key])  # prints the values of the dictionary using the keys    
    
      
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

def add_new_country(country, cities_visited, total_visits):
    travel_log[country] = {"cities_visited": cities_visited, "total_visits": total_visits}  
    
add_new_country("Russia", ["Moscow", "Saint Petersburg"], 2)
print(travel_log)   

print(travel_log["Russia"]["cities_visited"][1])



