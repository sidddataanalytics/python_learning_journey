
import random

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia",
 "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming"]
#print(states_of_america)
#print(states_of_america[0])
#print(states_of_america[-1])
#print(states_of_america[2])
#option 1
state = random.choice(states_of_america)
print(state)

#option 2
random_index = random.randint(0, len(states_of_america) - 1)
print(states_of_america[random_index])

#dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes"]
vegetables = ["Spinach", "Kale", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
