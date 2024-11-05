class single:
    def employee(self):
        self.name = "kartikeya"
        self.company = "google"
        print(f"the name is {self.name} and the company {self.company}")

class demo(single):
    def demoo(self):
        self.name = "kartik"

        self.company = "acenture"
        
        print(f"The name is {self.name} and company is {self.company}")


class programmer(demo):
    def show(self):
        self.name = "kartik"

        self.company = "acenture"
        
        print(f"The name is {self.name} and company is {self.company}")



a = programmer()
a.demoo()
a.employee()
a.show()