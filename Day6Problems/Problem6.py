m = int(input("Enter your marks"))
p = int(input("Enter your marks"))
c = int(input("Enter your marks"))
sum = m+p+c
total = sum/3
if(total>=90):
    print("excellent")

elif(total>=80):
    print("A")

elif(total>=70):
    print("B")

elif(total>=60):
    print("D grade")

else:
    print("Fail")

