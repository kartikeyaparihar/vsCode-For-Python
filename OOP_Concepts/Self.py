class Employee:
    lang = "py" 
    salary = 145667

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
#Employee.getInfo(kartik)  This kartik.getInfo is treated as this but in greet fuction there is no arguments and it is taken as
#Employee.greet(kartik) thats why it is not running if we give greet fuction a argument then it will fuction
# And if we dont want to pass argument in greet then we have to call greet fuction by class name 
# we can also make that fuction static so that we can call it also by ussind instance attribute

#Employee.greet()

