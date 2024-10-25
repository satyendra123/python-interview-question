# Creating a tuple with parentheses
my_tuple = (1, 2, 3, 4, 5)

# Tuple without parentheses (optional)
another_tuple = 1, 2, 3

# Single element tuple (note the comma)
single_element_tuple = (1,)

print(my_tuple)              # Output: (1, 2, 3, 4, 5)
print(another_tuple)         # Output: (1, 2, 3)
print(single_element_tuple)  # Output: (1,)


my_tuple = (10, 20, 30, 40, 50)

# Accessing elements by index
print(my_tuple[0])  # Output: 10
print(my_tuple[3])  # Output: 40

# Negative indexing
print(my_tuple[-1])  # Output: 50 (last element)
print(my_tuple[-2])  # Output: 40 (second-to-last element)


tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print(combined_tuple)  # Output: (1, 2, 3, 4, 5, 6)


my_tuple = (1, 2)
repeated_tuple = my_tuple * 3
print(repeated_tuple)  # Output: (1, 2, 1, 2, 1, 2)


my_tuple = (1, 2, 3, 4, 5)
sliced_tuple = my_tuple[1:4]
print(sliced_tuple)  # Output: (2, 3, 4)


my_tuple = (10, 20, 30)
print(len(my_tuple))  # Output: 3


# Unpacking tuple into variables
person = ("John", 30, "Engineer")

name, age, profession = person
print(name)       # Output: John
print(age)        # Output: 30
print(profession) # Output: Engineer


person = ("John", 30, "Engineer")

# Unpacking only name and profession, ignoring age
name, _, profession = person
print(name)        # Output: John
print(profession)  # Output: Engineer


my_tuple = (1, 2, 2, 3, 4, 2)
print(my_tuple.count(2))  # Output: 3


my_tuple = (10, 20, 30, 40, 30)
print(my_tuple.index(30))  # Output: 2 (first occurrence of 30)


def get_person_info():
    name = "Alice"
    age = 25
    profession = "Designer"
    return name, age, profession  # Returns a tuple

# Unpacking the returned tuple
name, age, profession = get_person_info()
print(name, age, profession)  # Output: Alice 25 Designer


# Tuple as dictionary keys
coordinates = {
    (0, 0): "origin",
    (1, 2): "point A",
    (3, 4): "point B"
}

print(coordinates[(1, 2)])  # Output: point A


# Packing values into a tuple
packed = ("John", 25, "Developer")

# Unpacking
name, age, job = packed
print(name, age, job)  # Output: John 25 Developer


import sys

my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

print(sys.getsizeof(my_list))   # Size of list in memory
print(sys.getsizeof(my_tuple))  # Size of tuple in memory


days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print(days_of_week[0])  # Output: Monday


