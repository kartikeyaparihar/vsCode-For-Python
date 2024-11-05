class employee:
    a = 1
    @classmethod
    def show(self):
        print(f"The value of a is {self.a}")
e = employee()
e.a = 45  #Instance attribute hasd given the priority
e.show()
#  But if we want to print the class attribute then we use class method

