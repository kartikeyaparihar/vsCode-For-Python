import random
computer = random.choice([1, -1, 0])
your_choice = input("Enter your choice \n choice : s\n Choice : w\n Choice : g\n Enter your choice :")
your_dict = {"s": 1 , "w": -1 , "g": 0}
reverse_dict = {1:"snake", -1 : "water" , 0 : "gun"}
you = your_dict[your_choice]
print(f"You choose {reverse_dict[you]} and computer choose {reverse_dict [computer]}")
'''
if(you == computer):
    print("Draw!")
                                     #Advanced analysis
else:
    if(computer == 1 or you == -1): #computer - you = 2
        print("you loose")
    elif(computer == 1 or you == 0):#computer - you = 1
        print("you win")
    elif(computer == -1 or you == 1):#computer - you = -2
        print("you win")
    elif(computer == -1 or you == 0):#computer - you = -1
        print("you loose")
    elif(computer == 0 or you == -1):#computer - you = 1
        print("you win")
    elif(computer == 0 or you == 1):#computer - you = -1
        print("you loose")
 
    else:
        print("something went wrong")
        '''

#Advanced analysis code :
if(computer - you == 1 or computer - you == -2):
    print("You win")
elif(computer == you):
    print("Draw")
else:
    print("You loose")

