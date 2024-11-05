a = int(input("Enter 1 number :"))
b = int(input("Enter 2 number :"))
c = int(input("Enter 3 number :"))
d = int(input("Enter 4 number :"))
if(a>b and a>c and a>d):
    print(a , "is the greatest number")

elif(b>c and b>a and b>d):
    print( b ,"is the greatest number")

elif(c>a and c>b and c>d):
    print(c ,"is the greatest number")

else:
    print(d ,"is the greatest number")