t = ("kartik",44,33,4,8,98,"hdh")
print(t.count("hdh"))

my_tuple = (1, 2, 3)
print(my_tuple[0])  # Output: 1

my_tuple = (1, 2, 3)
print(len(my_tuple))  # Output: 3

my_tuple = (1, 2, 3, 2)
index = my_tuple.index(3)
print(index)  # Output: 1

tuple1 = (1, 2)
tuple2 = (3, 4)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)  # Output: (1, 2, 3, 4)

my_tuple = (1, 2)
repeated_tuple = my_tuple * 3
print(repeated_tuple)  # Output: (1, 2, 1, 2, 1, 2)

my_tuple = (1, 2, 3)
for item in my_tuple:
    print(item)
# Output:
# 1
# 2
# 3

my_tuple = (1, 2, 3)
print(2 in my_tuple)  # Output: True
print(4 in my_tuple)  # Output: False

# Packing
my_tuple = 1, 2, 3
print(my_tuple)  # Output: (1, 2, 3)

# Unpacking
a, b, c = my_tuple
print(a, b, c)  # Output: 1 2 3
