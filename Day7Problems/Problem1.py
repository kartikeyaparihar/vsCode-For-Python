#Write a table of a number given by user
n = int(input("Enter the number for ewhich you want a table : "))

for i in range(1, 11):
    print(n, " x ",i,"=",n*i)

#while loop
n = int(input("Enter the number for ewhich you want a table : "))
i=1
while(i<11):
    print(f"{n} x {i} = {n*i}")
    i+=1
