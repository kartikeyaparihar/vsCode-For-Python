name = "kartikeya"
print(name.endswith("eya"))  #returns boolean
print(name.startswith("kart"))  #returns boolean  -->ALSO THIS FUNCTION IS CASE SENSITIVE


s = "Hello, World!"
print(s.upper())  # Output: "HELLO, WORLD!"
print(s.lower())  # Output: "hello, world!"

s = "   Hello, World!   "
print(s.strip())  # Output: "Hello, World!"

s = "apple,orange,banana"
print(s.split(","))  # Output: ['apple', 'orange', 'banana']

s = "Hello\nWorld\nPython"
print(s.splitlines())  # Output: ['Hello', 'World', 'Python']

words = ["Hello", "World", "Python"]
print(" ".join(words))  # Output: "Hello World Python"
 
s = "Hello, World!"
print(s.find("World"))  # Output: 7
print(s.index("World"))  # Output: 7

s = "Hello, World!"
print(s.replace("Hello", "Hi"))  # Output: "Hi, World!"

s = "Hello, World!"
print(s.startswith("Hello"))  # Output: True
print(s.endswith("World!"))   # Output: True

s1 = "12345"
s2 = "Hello"
s3 = "Hello123"
s4 = "   "

print(s1.isdigit())   # Output: True
print(s2.isalpha())   # Output: True
print(s3.isalnum())   # Output: True
print(s4.isspace())   # Output: True

name = "Alice"
age = 30
print("My name is {} and I am {} years old.".format(name, age))
# Output: "My name is Alice and I am 30 years old."

s = "hello, world!"
print(s.capitalize())   # Output: "Hello, world!"
print(s.title())        # Output: "Hello, World!"
print(s.swapcase())     # Output: "HELLO, WORLD!"
