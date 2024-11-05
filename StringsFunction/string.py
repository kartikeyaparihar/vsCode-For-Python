name = "kartikeya"
shortname = name[1:3]   #[a:b] here a is the starting index and till b is excluded
print(shortname)


                                              #k a r t i k e y a
                                              # 0 1 2 3 4 5 6 7 8
                                              #-9-8-7-6-5-4-3-2-1   ---> Negetive indexing  
print(name[-4:-1])
print(name[:3])  #[:3] means [0:3]
print(name[1:])  #[1:] means [1:9 or its length]
print(name[1:9]) 