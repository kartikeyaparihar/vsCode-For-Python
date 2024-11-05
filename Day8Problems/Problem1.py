# WRitw a program using funtions to find greatest of three numbers

def Greatest(a, b, c):
    if(a>b and a>c):
        print(f"{a} is the greatest number among {b} and {c}")
    elif(b>a and b>c):
        print(f"{b} is the greatest number among  {b} and {c}")
    else:
        print(f"{c} is the greatest")
a = int(input("Enter a number :"))
b = int(input("Enter a number :"))
c = int(input("Enter a number :"))
Greatest(a, b, c)