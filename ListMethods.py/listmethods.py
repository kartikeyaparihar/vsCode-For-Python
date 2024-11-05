l1 = ["kartik","ankur","bro","orkya","20",30,50]
l1.append("good") #append insert value at the end
print(l1)

l1.insert(4,45)  # Insert 45 at index 4
print(l1)

numbers = [1,5,3,88,97,55,43,2]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(numbers.pop(5))
print(numbers.remove(2))

my_list = [1, 2, 3]
another_list = [4, 5, 6]
my_list.extend(another_list)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]


my_list = [1, 2, 3, 2]
index = my_list.index(2)
print(index)  # Output: 1

my_list = [1, 2, 3, 2]
count = my_list.count(2)
print(count)  # Output: 2


my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # Output: []



