#Import random number generator and generate index of computer's choice of rock, paper, or scissors.
import random
index = random.randint(0,2)
#Initialize computer's choice as an empty string.
computer = ""
#Allow computer to determine choice of Rock, Paper, or Scissors, based on index generated
#via random number generator.
if(index==0):
    computer = "Rock"
elif(index==1):
    computer = "Paper"
else:
    computer = "Scissors"

#Request of user for input of Rock, Paper, or Scissors.
user_input = input("Please enter choice of Rock, Paper, or Scissors (as they are printed in this line of instruction): ")

#If user makes decision not granted in program, continually requests of them
#to make valid decision of Rock, Paper, or Scissors, until they do.
if(user_input != "Rock" and user_input != "Paper" and user_input != "Scissors"):
    while(user_input != "Rock" and user_input != "Paper" and user_input != "Scissors"):
        user_input = input("I apologize. That option is not a choice given. Please input option of "
              + " Rock, Paper, or Scissors (as they are given in this line of instruction): ")

#Continually runs program in the case of tie between player and computer until tie
#is settled by allowing the player to change their answer and allowing computer to change its answer
#in the same manner it first generated its initial answer.

if(user_input==computer):
    while(user_input==computer):
        user_input = input("I apologize. I believe we have a tie. Please try again and give input of "
                           + "Rock, Paper, or Scissors (as they are given in this line of instruction)")
        index = random.randint(0,2)
        #Initialize computer's choice as an empty string.
        computer = ""
        #Allow computer to determine choice of Rock, Paper, or Scissors, based on index generated
        #via random number generator.
        if(index==0):
            computer = "Rock"
        elif(index==1):
            computer = "Paper"
        else:
            computer = "Scissors"    

#Determines if player won or lost game, depending on difference of their
#answer in relation to randomly generated answer of computer.
if(user_input=="Rock"):
    if(computer=="Paper"):
        print("I am sorry. You lose. The computer picked paper. Game Over!")
    else:
        print("Congratulations! You won! The computer picked Scissors. Game Over!")

if(user_input=="Paper"):
    if(computer=="Rock"):
        print("Congratulations! You won! The computer picked Rock. Game Over!")
    else:
        print("I am sorry. You lose. The computer picked Scissors. Game Over!")

if(user_input=="Scissors"):
    if(computer=="Rock"):
        print("Congratulations! You win! The computer picked Rock. Game Over!")
    else:
        print("I am sorry. You lose. The computer picked Paper. Game Over!")
