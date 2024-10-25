#EX-1
my_set = {1, 2, 3, 4, 5}
empty_set = set()
print(my_set)
print(empty_set)

#EX-2
my_set = {1, 2, 2, 3, 4}
print(my_set)                         # o/p= 1,2,3,4

#EX-3
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)                         #o/p = 1,2,3,4

#EX-4
my_set = {1, 2, 3}
my_set.remove(2)     # Removes element 2
# my_set.remove(5)   # Will raise an error (KeyError)
my_set.discard(5)    # No error, even if 5 is not present

my_set = {1, 2, 3}
print(2 in my_set)    # Output: True
print(5 in my_set)    # Output: False


set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print(union_set)  # Output: {1, 2, 3, 4, 5}


set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1 & set2
print(intersection_set)  # Output: {3}


set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1 - set2
print(difference_set)  # Output: {1, 2}


set1 = {1, 2, 3}
set2 = {3, 4, 5}
symmetric_diff_set = set1 ^ set2
print(symmetric_diff_set)  # Output: {1, 2, 4, 5}


my_list = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(my_list)
print(unique_set)  # Output: {1, 2, 3, 4, 5}


list1 = [1, 2, 3]
list2 = [3, 4, 5]
common = set(list1) & set(list2)
print(common)  # Output: {3}


my_list = [1, 2, 3, 4, 5]
my_set = set(my_list)
print(3 in my_set)  # Output: True
print(10 in my_set) # Output: False
