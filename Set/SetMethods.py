s = {1,5,5,32,44,23,5,6,7,8,9}
print(s)
s.add("kartik")
print(s)

my_set = {1, 2, 3}
my_set.clear()
print(my_set)  # Output: set()

my_set = {1, 2, 3}
new_set = my_set.copy()
print(new_set)  # Output: {1, 2, 3}

set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.difference(set2))  # Output: {1}

set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.difference_update(set2)
print(set1)  # Output: {1}

my_set = {1, 2, 3}
my_set.discard(2)
print(my_set)  # Output: {1, 3}

# Discarding an element not in the set does nothing
my_set.discard(4)
print(my_set)  # Output: {1, 3}

set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.intersection(set2))  # Output: {2, 3}

set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.intersection_update(set2)
print(set1)  # Output: {2, 3}

set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.isdisjoint(set2))  # Output: True

set3 = {3, 4, 5}
print(set1.isdisjoint(set3))  # Output: False

set1 = {1, 2}
set2 = {1, 2, 3}
print(set1.issubset(set2))  # Output: True

set3 = {2, 3}
print(set1.issubset(set3))  # Output: False

set1 = {1, 2, 3}
set2 = {1, 2}
print(set1.issuperset(set2))  # Output: True

set3 = {2, 4}
print(set1.issuperset(set3))  # Output: False

my_set = {1, 2, 3}
element = my_set.pop()
print(element)  # Output could be 1, 2, or 3 (arbitrary)
print(my_set)  # Output will be the set without the popped element

my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)  # Output: {1, 3}

# Trying to remove an element not in the set raises KeyError
# my_set.remove(4)  # This will raise KeyError

set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.symmetric_difference(set2))  # Output: {1, 4}

set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.symmetric_difference_update(set2)
print(set1)  # Output: {1, 4}

set1 = {1, 2}
set2 = {2, 3}
print(set1.union(set2))  # Output: {1, 2, 3}

set1 = {1, 2}
set2 = {2, 3}
set1.update(set2)
print(set1)  # Output: {1, 2, 3}

print(len(s))