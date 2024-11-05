#write a program to using functions to print a table of a given number
def table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")
n = int(input("Enter a number for which you want a table"))
table(n)