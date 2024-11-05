class single:
    def employee(self):
        self.name = "kartikeya"
        self.company = "google"
        print(f"the name is {self.name} and the company {self.company}")

class programmer(single):
    def show(self):
        self.name = "kartik"

        self.company = "acenture"
        
        print(f"The name is {self.name} and company is {self.company}")

a = programmer()
a.employee()
a.show()

    