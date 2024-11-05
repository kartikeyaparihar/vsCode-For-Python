def rem(l, word):
    for item in l:
        l.remove(word)
        return l
l = ["harry","kartik","rohan","subh"]
print(rem(l, "an"))