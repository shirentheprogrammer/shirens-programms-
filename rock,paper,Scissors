# @Copyright Shiren Thapa
# MIT General Purpose Licensing
import time 
from cgi import print_directory
import random

possible_actions = ["rock", "paper", "scissors"]
numberofruns = int(input("How many times do you want it to run Hint, if your doing many rounds, don't get details!"))
shouldPrintDetails = input("Do you want details? (0 (No) 1 (Yes)")

computer1_wins=0
computer2_wins=0
computer_ties=0

def printDetails(shouldPrintDetails1,printInfo):
    if shouldPrintDetails1 == "1":
        print(printInfo)
        

for x in range(0,numberofruns):
    print()
    print(f"MATCH Number {x}") 
    computer1_action = random.choice(possible_actions)
    computer2_action = random.choice(possible_actions)
    printDetails(shouldPrintDetails,f"\tComputer 1 Chose {computer1_action}.")
    printDetails(shouldPrintDetails,(f"\tComputer 2 Chose {computer2_action}.")) 
    if computer1_action == computer2_action:
        printDetails(shouldPrintDetails,(f"\t\tBoth players selected {computer1_action}. It's a tie!"))
        computer_ties+=1
    elif computer1_action == "rock":
        if computer2_action == "scissors":
            printDetails(shouldPrintDetails,("\t\tRock smashes scissors! Computer 1 wins!"))
            computer1_wins+=1
        else:
            printDetails(shouldPrintDetails,("\t\tPaper covers rock! Computer 2 wins."))
            computer2_wins+=1
    elif computer1_action == "paper":
        if computer2_action == "rock":
            printDetails(shouldPrintDetails,("\t\tPaper covers rock! Computer 1 wins!"))
            computer1_wins+=1
        else:
            printDetails(shouldPrintDetails,("\t\tScissors cuts paper! Computer 2 wins!"))
            computer2_wins+=1
    elif computer1_action == "scissors":
        if computer2_action == "paper":
            printDetails(shouldPrintDetails,("\t\tScissors cuts paper! Computer 1 Wins!"))
            computer1_wins+=1
        else:
            printDetails(shouldPrintDetails,("\t\tRock smashes scissors! Computer 2 Wins!"))
            computer2_wins+=1
            
            
print()          
print(f"Computer 1 won {str(computer1_wins)} times out of {str(numberofruns)}")
print(f"Computer 2 won {str(computer2_wins)} times out of {str(numberofruns)}")
print(f"The computers tied {str(computer_ties)}  times out of {str(numberofruns)}")
print()

time.sleep(5)


import random


print("Winning Rules of the Rock paper scissor game as follows: \n"
								+"Rock vs paper->paper wins \n"
								+ "Rock vs scissor->Rock wins \n"
								+"paper vs scissor->scissor wins \n")

while True:
	print("Enter choice \n 1 for Rock, \n 2 for paper, and \n 3 for scissor \n")
	
	choice = int(input("User turn: "))


	while choice > 3 or choice < 1:
		choice = int(input("enter valid input: "))
		

	if choice == 1:
		choice_name = 'Rock'
	elif choice == 2:
		choice_name = 'paper'
	else:
		choice_name = 'scissor'
		

	print("user choice is: " + choice_name)
	print("\nNow its computer turn.......")


	comp_choice = random.randint(1, 3)
	
	
	while comp_choice == choice:
		comp_choice = random.randint(1, 3)

	
	if comp_choice == 1:
		comp_choice_name = 'Rock'
	elif comp_choice == 2:
		comp_choice_name = 'paper'
	else:
		comp_choice_name = 'scissor'
		
	print("Computer choice is: " + comp_choice_name)

	print(choice_name + " V/s " + comp_choice_name)


	if((choice == 1 and comp_choice == 2) or
	(choice == 2 and comp_choice ==1 )):
		print("paper wins => ", end = "")
		result = "paper"
		
	elif((choice == 1 and comp_choice == 3) or
		(choice == 3 and comp_choice == 1)):
		print("Rock wins =>", end = "")
		result = "Rock"
	else:
		print("scissor wins =>", end = "")
		result = "scissor"

	
	if result == choice_name:
		print("<== User wins ==>")
	else:
		print("<== Computer wins ==>")
		
	print("Do you want to play again? (Y/N)")
	ans = input()



	if ans == 'n' or ans == 'N':
		break
	

print("\nThanks for playing")



again = 'y'

while (again == 'y'):

    p1 = input("Player 1 --> Rock, Paper, or Scissors? ")
    p1 = p1.lower()

    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()



    




    p2 = input("Player 2 --> Rock, Paper, or Scissors? ")
    p2 = p2.lower()

    print()

    if (p1 == "rock"):
        if (p2 == "rock"):
            print("The game is a draw")
        elif (p2 == "paper"):
            print("Player 2 wins!")
        elif (p2 == "scissors"):
            print("Player 1 wins!")
    elif (p1 == "paper"):
        if (p2 == "rock"):
            print("Player 1 wins!")
        elif (p2 == "paper"):
            print("The game is a draw")
        elif (p2 == "scissors"):
            print("Player 2 wins!")
    elif (p1 == "scissors"):
        if (p2 == "rock"):
            print("Player 2 wins!")
        elif (p2 == "paper"):
            print("Player 1 wins!")
        elif (p2 == "scissors"):
            print("The game is a draw")
    else:
        print("Invalid input, try again")

    again = input("Type y to play again, anything else to stop: ")

    print()


print("have a good day!  ")

    
