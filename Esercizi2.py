#2-3. Personal Message:
name = "Michele"  
message = f"Hello {name.title()}, would you like to learn some Python today?"
print(message)


#2-4. Name Cases:
name = "Michele"
print(f"Lowercase: {name.lower()}")
print(f"Uppercase: {name.upper()}")
print(f"Title Case: {name.title()}")


#2-5. Famous Quote:
author = "Maya Angelou"
quote = "Still I rise."
print(f"{author} once said, \"{quote}\"")


#2-6. Famous Quote 2:
famous_person = "Marie Curie"
message = f"{famous_person} once said, \"The important thing is not to stop questioning. Curiosity has its own reason for existing.\""
print(message)#


#2-8. File Extensions:
filename = "python_notes.txt"
no_extension = filename.removesuffix(".txt")
print(f"Filename without extension: {no_extension}")


#3-1. Names:
names = ["Michele", "Sandro", "Marco"]
for name in names:
    print(f"Hello, {name}!")


#3-2. Greetings:
names = ["Michele", "Sandro", "Marco"]
for name in names:
    print(f"Greetings, {name.title()}! How are you doing today?")


#3-3. Your Own List:
vehicles = ["Moto", "Auto", "Aereo"]
for vehicle in vehicles:
    print(f"I would love to own a {vehicle.title()}.")

#3-4. Guest List:
guests = ["Albert Einstein", "Marie Curie", "Stephen Hawking"]
for guest in guests:
    print(f"Dear {guest}, I would be honored to have you join me for dinner")


#3-5. Changing Guest List:
guests = ["Albert Einstein", "Marie Curie", "Stephen Hawking"]
declining_guest = guests.pop()  

print(f"\nUnfortunately, {declining_guest} won't be able to make it.")

guests.append("Isaac Asimov")  

for guest in guests:
    print(f"Dear {guest}, I would be honored to have you join me for dinner.")


#3-6. More Guests:
guests = ["Albert Einstein", "Marie Curie", "Stephen Hawking"]
print("\nI found a bigger table! Let's invite more guests.")

guests.insert(0, "Ada Lovelace")  
guests.insert(2, "Alan Turing")   
guests.append("Blaise Pascal")   

for guest in guests:
    print(f"Dear {guest}, I would be honored to have you join me for dinner.")


#3-7. Shrinking Guest List:
guests = ["Albert Einstein", "Marie Curie", "Stephen Hawking",
          "Ada Lovelace", "Alan Turing", "Blaise Pascal"]
print("\nUnfortunately, there's only space for two guests at my table.")

while len(guests) > 2:
    declined_guest = guests.pop()
    print(f"Dear {declined_guest}, I'm so sorry, but there's no longer room for you at dinner.")

remaining_guests = guests.copy()  
for guest in remaining_guests:
    print(f"Dear {guest}, you're still invited to dinner!")

del guests[:]  
print(f"\nGuest list: {guests}")


#3-8. Seeing the World:
luoghi_da_visitare = ["Grande Barriera Corallina", "Macchu Picchu", "Islanda", "Kenya", "Isole Galapagos"]

print("Lista originale:", luoghi_da_visitare)


print("Ordinata (crescente):", sorted(luoghi_da_visitare))


print("Lista originale (invariata):", luoghi_da_visitare)


print("Ordinata (decrescente):", sorted(luoghi_da_visitare, reverse=True))


print("Lista originale (invariata):", luoghi_da_visitare)


luoghi_da_visitare.reverse()
print("Lista invertita:", luoghi_da_visitare)


luoghi_da_visitare.reverse()
print("Ordine originale ripristinato:", luoghi_da_visitare)


luoghi_da_visitare.sort()
print("Ordinata permanentemente (crescente):", luoghi_da_visitare)


luoghi_da_visitare.sort(reverse=True)
print("Ordinata permanentemente (decrescente):", luoghi_da_visitare)


#3-9. Dinner Guests:
invitati_cena = ["Marco", "Luca", "Carlo"]
numero_invitati = len(invitati_cena)
print(f"Stai invitando {numero_invitati} persone a cena.")


#3-10. Every Function: Lists
def create_list(items):

    new_list = list(items)
    return new_list

mountains = ["Everest", "K2", "Kangchenjunga"]
rivers = ["Nile", "Amazon", "Yangtze"]

mountain_list = create_list(mountains)
river_list = create_list(rivers)

print("Mountains:", mountain_list)
print("Rivers:", river_list)

#6-1. Person: Dictionary
def create_person_dict(first_name, last_name, age, city):
    
    person = {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "city": city
    }
    return person


person = create_person_dict("Alice", "Luca", 30, "New York")

print("First Name:", person["first_name"])
print("Last Name:", person["last_name"])
print("Age:", person["age"])
print("City:", person["city"])


#6-2. Favorite Numbers: Dictionary
def favorite_numbers_dict():
    
    favorite_numbers = {
        "Alice": [3, 7],
        "Luca": 11,
        "Charlie": 21,
        "Davide": [5, 13],
        "Sara": 42
    }
    return favorite_numbers

favorites = favorite_numbers_dict()

for name, numbers in favorites.items():
    if len(numbers) > 1:
        print(f"{name}'s favorite numbers are: {', '.join(map(str, numbers))}")
    else:
        print(f"{name}'s favorite number is: {numbers[0]}")


#6-3. Glossary: Dictionary
def programming_glossary():
    

    glossary = {
        "variable": "A named storage location for data.",
        "list": "An ordered collection of items that can be changed.",
        "dictionary": "An unordered collection of key-value pairs.",
        "function": "A block of reusable code that performs a specific task.",
        "loop": "A control flow structure that repeatedly executes a block of code."
    }
    return glossary
terms = programming_glossary()

for term, meaning in terms.items():
    print(f"{term}:\n{meaning}\n")


#6-7. People: List of Dictionaries
people = [
    {
        "nome": "Luca",  
        "cognome": "Rossi", 
        "eta": 22,
    },
    {
        "nome": "Alice",  
        "cognome": "Bianchi",  
        "eta": 23,
    },
    {
        "nome": "Matteo",  
        "cognome": "Verdi",  
        "eta": 25,
    },
]

for person in people:
    print(f"Nome: {person['nome']}")
    print(f"Cognome: {person['cognome']}")
    print(f"Età: {person['eta']}")
    print("\n")


#6-8. Pets:
pets = [
    {"animal": "dog", "owner": "Michael"},
    {"animal": "cat", "owner": "Sarah"},
    {"animal": "fish", "owner": "Emily"},
]

for pet in pets:
    print(f"Animal: {pet['animal']}")
    print(f"Owner: {pet['owner']}")
    print("\n")


#6-9. Favorite Places
favorite_places = {
    "Luca": ["Paris", "New York"],
    "Marco": ["Tokyo", "London"],
    "Alice": ["Rome", "Barcelona", "Berlin"],
}

for person, places in favorite_places.items():
    print(f"{person}'s favorite places are:")
    for place in places:
        print(f"\t{place}")
    print("\n")


#6-10. Favorite Numbers:
people = {
    "Alice": [7, 3],
    "Marco": [18, 12],
    "Matteo": [25, 4],
}

for person, numbers in people.items():
    print(f"{person}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")
    print("\n")


#6-11. Cities:
cities = {
    "Tokyo": {
        "country": "Japan",
        "population": "37.4 million",
        "fact": "It is the most populous metropolitan area in the world."
    },
    "New York City": {
        "country": "United States",
        "population": "8.8 million",
        "fact": "The Statue of Liberty was a gift from France to the US."
    },
    "London": {
        "country": "England",
        "population": "8.9 million",
        "fact": "Big Ben is the nickname for the clock tower at the Palace of Westminster."
    }
}

for city, info in cities.items():
    print(f"\nCity: {city}")
    print(f"\tCountry: {info['country']}")
    print(f"\tPopulation: {info['population']}")
    print(f"\tFact: {info['fact']}")


#6-12. Extensions:
favorite_places = {
    "Alice": {
        "vacation_spots": ["Paris", "New York"],
        "weekend_getaways": ["Beach", "Mountains"],
    },
    "Marco": {
        "vacation_spots": ["Tokyo", "London"],
        "weekend_getaways": ["Forest", "Lake"],
    },
    "Luca": {
        "vacation_spots": ["Rome", "Barcelona"],
        "weekend_getaways": ["City Breaks", "Historical Sites"],
    },
}

for person, places in favorite_places.items():
    print(f"{person}'s favorite places:")
    for category, locations in places.items():
        print(f"\t{category.title()}:")
        for location in locations:
            print(f"\t\t{location}")
    print("\n")






