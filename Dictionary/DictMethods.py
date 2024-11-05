marks = {
    "kartik": 78,
    "subh": 82,
    "honey":64
}
print(marks.items())  #Dict is mutable and here in mark.items items returns the value in Tuple form
print(marks.keys())
print(marks.update(({"kartik":100, "renu":99})),marks)
print(marks.values())
print(marks.get("subh"))

my_dict = {'a': 1, 'b': 2}
print(my_dict.pop('a'))  # Output: 1
print(my_dict)  # Output: {'b': 2}

my_dict = {'a': 1, 'b': 2}
print(my_dict.popitem())  # Output: ('b', 2)
print(my_dict)  # Output: {'a': 1}

my_dict = {'a': 1, 'b': 2}
my_dict.clear()
print(my_dict)  # Output: {}

my_dict = {'a': 1, 'b': 2}
new_dict = my_dict.copy()
print(new_dict)  # Output: {'a': 1, 'b': 2}

keys = ['a', 'b', 'c']
new_dict = dict.fromkeys(keys, 0)
print(new_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}

my_dict = {'a': 1}
print(my_dict.setdefault('b', 2))  # Output: 2
print(my_dict)  # Output: {'a': 1, 'b': 2}

# Key 'a' is already in the dictionary, so its value is returned
print(my_dict.setdefault('a', 99))  # Output: 1

print(marks.get("kartik"))#gives none if name is diff
print(marks["kartik"]) #But this gives an error