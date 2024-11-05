class employee:
    a = 1
    @classmethod
    def show(self):
        print(f"The value of a is {self.a}")

    @property
    def name(self):
        return f" {self.fname} {self.lname}"
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0] 
        self.lname = value.split(" ")[1]                  # a = kartik parihar
                                               # a.spilt(" ")   ----> ["kartik","parihar"]
e = employee()
e.name = "kartik parihar"
print(e.name)
#e.a = 45  #Instance attribute hasd given the priority
#e.show()