#8-1. Message: 
def display_message():
  print("In this chapter, I am learning about Python!")

display_message()


#8-2. Favorite Book:
def favorite_book(title):
  print("One of my favorite books is", title)

favorite_book("The Hitchhiker's Guide to the Galaxy")


#8-3. T-Shirt: 
def make_shirt(size, message):
  print("You've ordered a " + size + " shirt that says '" + message + "'")

make_shirt('large', 'I love Python!')
make_shirt(message='Do or do not, there is no try.', size='medium')


#8-4. Large Shirts: 
def make_shirt(size='large', message="I love Python"):
  print("You've ordered a " + size + " shirt that says '" + message + "'")

make_shirt()  
make_shirt(size='medium')  
make_shirt(message="Do or do not, there is no try.", size='small')  


#8-5. Cities:
def describe_city(city, country="USA"):
  print(city.title() + " is located in " + country)

describe_city("Tokyo", "Japan")
describe_city("Berlin")
describe_city("Buenos Aires", "Argentina")


#8-6. City Names: 
def city_country(city, country):
  return city.title() + ", " + country.title()

place = city_country("santiago", "chile")
print(place)

place = city_country("berlin", "germany")
print(place)

place = city_country("new york city", "usa")
print(place)


#8-7. Album:
def make_album(artist_name, album_title, number_of_songs=None):
  album = {'artist': artist_name, 'title': album_title}
  if number_of_songs:
    album['songs'] = number_of_songs
  return album

album1 = make_album('Pink Floyd', 'The Dark Side of the Moon')
print(album1)

album2 = make_album('Kendrick Lamar', 'To Pimp a Butterfly', 16)
print(album2)

album3 = make_album('The Beatles', 'Abbey Road')
print(album3)


#8-8. User Albums:
def make_album(artist_name, album_title, number_of_songs=None):
  album = {'artist': artist_name, 'title': album_title}
  if number_of_songs:
    album['songs'] = number_of_songs
  return album

while True:
  print("\nEnter 'q' to quit.")
  artist_name = input("Artist name: ")
  if artist_name.lower() == 'q':
    break

  album_title = input("Album title: ")

  number_of_songs = input("Number of songs (optional): ")
  if number_of_songs.isdigit():
    number_of_songs = int(number_of_songs)
  else:
    number_of_songs = None

  album = make_album(artist_name, album_title, number_of_songs)
  print(album)

print("\nThanks for using the Album Creator!")


#8-9. Messages:
def show_messages(messages):
  print("\nShowing messages:")
  for message in messages:
    print("-", message)

messages = ["Hello!", "How are you?", "Goodbye!"]
show_messages(messages)


#8-10. Sending Messages:
def show_messages(messages):
  print("\nShowing messages:")
  for message in messages:
    print("-", message)

def send_messages(messages, sent_messages):
  print("\nSending messages:")
  while messages:
    current_message = messages.pop()
    print("-", current_message)
    sent_messages.append(current_message)

messages = ["Hello!", "How are you?", "Goodbye!"]
sent_messages = []

show_messages(messages)  

send_messages(messages, sent_messages)  

print("\nOriginal messages:")
show_messages(messages)  

print("\nSent messages:")
show_messages(sent_messages)  


#8-11. Archived Messages:
def show_messages(messages):
  print("\nShowing messages:")
  for message in messages:
    print("-", message)

def send_messages(messages, sent_messages):
  print("\nSending messages:")
  while messages:
    current_message = messages.pop()  
    print("-", current_message)
    sent_messages.append(current_message)

messages = ["Hello!", "How are you?", "Goodbye!"]
sent_messages = []

original_messages = messages[:]  

show_messages(messages) 

send_messages(messages, sent_messages) 

print("\nOriginal messages:")
show_messages(original_messages)  )

print("\nSent messages:")
show_messages(sent_messages)  


#8-12. Sandwiches:
def make_sandwich(*sandwich_ingredients):
  print("\nYou ordered a sandwich with:")
  if not sandwich_ingredients:
    print("\tNothing (you rebel)")
  else:
    for ingredient in sandwich_ingredients:
      print(f"\t-{ingredient}")

make_sandwich("bread", "cheese", "turkey")
make_sandwich("roast beef", "mustard")
make_sandwich("peanut butter", "jelly")


#8-13. User Profile:
def build_profile(first_name, last_name, purpose, knowledge_base, parameters):
  return f"{first_name} {last_name}, purpose: {purpose}, knowledge base: {knowledge_base}, parameters: {parameters}"

my_profile = build_profile(
    first_name="Bard", last_name="", purpose="Large language model", knowledge_base="Text and code", parameters="137B parameters")
print(my_profile)


#8-14. Cars: 
def make_car(manufacturer, model, **other_info):
  car_info = {'manufacturer': manufacturer, 'model': model}
  car_info.update(other_info)
  return car_info

my_car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_car)


#8-15. Printing Models:
def print_model(model_name, formatted=False):
  if formatted:
    print(f"We are printing the model: {model_name}")
  else:
    print(model_name)

def print_models(unprinted_models, completed_models):
  
  print("\nUnprinted Models:")
  for model_name in unprinted_models:
    print_model(model_name)

  print("\nCompleted Models:")
  for model_name in completed_models:
    print_model(model_name, formatted=True)

from printing_functions import print_model, print_models

unprinted_models = ['iphone case', 'robot pendant']
completed_models = ['dog tag']

print_models(unprinted_models, completed_models)


#8-16. Imports: 
def greet(name):
  print(f"Hello, {name}!")


from function_file import greet

from function_file import greet as hello


import function_file as greetings


greet("Alice")  

hello("Bob")  

greetings.greet("Charlie")  


#8-17. Styling Functions: 

#1. make_car function (Exercise 8-14):
def make_car(manufacturer, model, **other_info):
    car_info = {'manufacturer': manufacturer, 'model': model}
    car_info.update(other_info)
    return car_info

#2. greet function (Exercise 8-16):
def greet(name):
    print(f"Hello, {name}!")

#3. print_models function (Exercise 8-15):
def print_models(unprinted_models, completed_models):
    
    print("\nUnprinted Models:")
    for model_name in unprinted_models:
        print_model(model_name)

    print("\nCompleted Models:")
    for model_name in completed_models:
        print_model(model_name, formatted=True)










