f = open("ex.txt","w")
f.write("hey")
print(f.read())
f.close()

# THe same can be done by using with statement
with open("ex.txt") as f:
    print(f.read())

#You dont have to explicitly close the file         