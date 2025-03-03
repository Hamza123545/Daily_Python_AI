# Tuple example
t1 = (1, 2, 3)
t2 = (1, 2, 3)
t3 = t1  # Both t1 and t3 refer to the same object

print("Tuple Check:\n")
print(t1 is t2, "\n")  # False (Different memory locations)
print(t1 is t3, "\n")  # True (Same object)

# Set example
s1 = {10, 20, 30}
s2 = {10, 20, 30}

print("Set Check:\n")
print(s1 is s2, "\n")  # False (Different memory locations)

# Dictionary example
d1 = {"name": "Hamza"}
d2 = {"name": "Hamza"}
d3 = d1  # d3 is the same as d1

print("Dictionary Check:\n")
print(d1 is d2, "\n")  # False (Different objects)
print(d1 is d3, "\n")  # True (Same object)



# Tuple example
tup = (5, 10, 15, 20)
print("Tuple Check:\n")
print(10 in tup, "\n")  # True (10 exists)
print(50 in tup, "\n")  # False (50 not in tuple)

# Set example
s = {100, 200, 300}
print("Set Check:\n")
print(200 in s, "\n")  # True (200 exists in set)
print(500 in s, "\n")  # False (500 not in set)

# Dictionary example (Checks keys, not values!)
dic = {"name": "Ali", "age": 25}
print("Dictionary Check:\n")
print("name" in dic, "\n")  # True (Key exists)
print("Ali" in dic, "\n")  # False (Checks only keys, not values)
