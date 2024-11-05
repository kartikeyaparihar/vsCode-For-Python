'''f = open("try.txt")
lines = f.readline()
print(lines,type(lines))
f.close()
'''
#Append --> add at last

st = "hey you are amazing"
f = open("myfile.txt", "a")
f.write(st)
f.close()