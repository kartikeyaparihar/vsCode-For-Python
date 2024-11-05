letter = ''' Dear <|Nmae|>,
             you are selected!
             <|Date|>'''
print(letter.replace("<|Nmae|>", "kartik").replace("<|Date|>", "2july"))
#IF WE WRITE print(letter) it will returns the first string without replacing because string is immutable
