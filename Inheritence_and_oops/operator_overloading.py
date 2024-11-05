'''class overload:
    def __init__(self,n):
        self.n = n

n = overload(1)
m = overload(2)

print(n+m)
#gives error'''

class overload:
    def __init__(self,n):
        self.n = n
    def _add_(self,num):
        self.n = num.n
n = overload(1)
m = overload(2)
print(n+m)

        