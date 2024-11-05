#write a class calculator capable of finding square , cube , and square root of a number
class calculator:
    number = int(input("Enter any number"))
    square = number*number
    cube = number*number*number
    square_root = number**1/2
    def __init__(self,square,cube,square_root):
        self.square = square
        self.cube = cube
        self.square_root = square_root

    print(f"Square of your number {number} is {square} \n cube of your number {number} is {cube}\n and lastly square root of your number {number} is {square_root} ")
        
