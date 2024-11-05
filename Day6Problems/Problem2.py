# Write a program whether a student passed or fail
m = int(input("enter your marks"))
p = int(input("enter your marks"))
c = int(input("enter your marks"))

total = m+p+c

result = (total/300)*100

if(m>33  and p>33 and c>33 and result>40):
    print("You are passed ",result)

else:
    print("oops!")
