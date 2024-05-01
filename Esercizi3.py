#4-1. Pizzas:
favorite_pizzas = ["Diavola", "Romana", "Margherita"]

for pizza in favorite_pizzas:
  print(f"I like {pizza.lower()} pizza.")

print("I really love pizza!")


#4-2. Animals: 
feline_friends = ["Lion", "Cheetah", "Puma"]

for feline in feline_friends:
  print(f"{feline} is a magnificent feline!")  

print("Felines are predetors!")  


#4-3. Counting to Twenty:
for number in range(1, 21):
  print(number)


#4-4. One Million:
million_numbers = list(range(1, 1000001))
print(million_numbers[:10])  
print("...")  
print(million_numbers[-10:])  


#4-5. Summing a Million:
million_numbers = list(range(1, 1000001))

print(f"Minimum: {min(million_numbers)}")
print(f"Maximum: {max(million_numbers)}")
total_sum = sum(million_numbers)
print(f"Sum of 1 to 1,000,000: {total_sum}")


#4-6. Odd Numbers:
odd_numbers = list(range(1, 21, 2))  
for number in odd_numbers:
  print(number)


#4-7. Threes:
threes = list(range(3, 31, 3)) 
for number in threes:
  print(number)


#4-8. Cubes:
cubes = [number**3 for number in range(1, 11)]
for cube in cubes:
  print(cube)


#4-9. Cube Comprehension:
cubes = [number**3 for number in range(1, 11)]  # Same as 4-8
print(cubes)


#4-10. Slices:


#4-11. My Pizzas, Your Pizzas:
my_pizzas = ["pepperoni", "cheese", "Hawaiian"]
friend_pizzas = my_pizzas[:]  
my_pizzas.append("veggie")
friend_pizzas.append("mushroom")
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)


#4-12. More Loops:
my_fruits = ["apple", "banana", "cherry"]
my_vegetables = ["carrot", "pea", "lettuce"]

print("My favorite fruits are:")
for fruit in my_fruits:
    print(fruit)

print("\nMy favorite vegetables are:")
for vegetable in my_vegetables:
    print(vegetable)

