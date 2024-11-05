# create a class "programmer" for storing a informationmof few prpgrammers working at microsoft
class programmer:
    company = "microsoft"
    def __init__(self,name,salary,pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode

p = programmer("kartik",120000000,465669)
print(p.name,p.salary,p.company,p.pincode)

r= programmer("rohit",120000000,465669)
print(r.name,r.salary,r.company,r.pincode)


        