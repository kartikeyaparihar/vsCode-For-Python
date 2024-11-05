class single:
    def __init__(self):
        self.name = "kartikeya"
        self.company = "google"
        print(f"the name is {self.name} and the company {self.company}")

class demo():
    def __init__(self):
        self.name = "kartik"
        self.company = "acenture"
        
        print(f"The name is {self.name} and company is {self.company}")


class programmer(single,demo):
    def show(self):
        self.name = "kartik"
        super().__init__()

        self.company = "acenture"
        
        print(f"The name is {self.name} and company is {self.company}")



a = programmer()
#a.demoo()
#a.employee()
a.show()