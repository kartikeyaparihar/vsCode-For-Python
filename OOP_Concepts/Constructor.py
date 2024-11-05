class Employee:
    lang = "py" 
    salary = 145667

    def __init__(self):  #This is a dunder method which does not needs to be called
        print("I am creating an object")
        

    def getInfo(self):
        print(f"The language is {self.lang} and salary is {self.salary} ")
    @staticmethod
    def greet():
        print("Good day sir")

kartik = Employee()
#kartik.name = "kartik" #This is an intance attribute
#print(kartik.name,kartik.salary,kartik.lang)
kartik.greet()
kartik.getInfo()