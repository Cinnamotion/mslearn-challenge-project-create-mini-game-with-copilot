#  make a rock paper scissors game with multiplayer, where the computer will be your opponent and can randomly choose one of the elements (rock, paper, or scissors) for each move, just like you. Your interaction in the game will be through the console (Terminal). The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option. At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent. By the end of each round, the player can choose whether to play again. Display the player's score at the end of the game. The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.
# 
# You can use the following code as a starting point:
# 
# ```python
from random import randint

# create a list of play options
t = ["rock", "paper", "scissors"]

# assign a random play to the computer
computer = t[randint(0,2)]

# set player to False
playing = True
player = ""
score = 0

#refactor all the rock paper and scissors words below to be lowercase

while playing:
# set player to True
    while player not in t:
        player = input("Rock, Paper, Scissors? ").lower()
        if player == computer:
            print("Tie!")
        elif player == "rock":
            if computer == "paper":
                print("You lose!", computer, "covers", player)
            else:
                score += 1
                print("You win!", player, "smashes", computer)
        elif player == "paper":
            if computer == "scissors":
                print("You lose!", computer, "cut", player)
            else:
                score += 1
                print("You win!", player, "covers", computer)
        elif player == "scissors":
            if computer == "rock":
                print("You lose...", computer, "smashes", player)
            else:
                score += 1
                print("You win!", player, "cut", computer)
        else:
            print("That's not a valid play. Check your spelling!")

    playing = input("Play again? (y/n) ").lower()
    if playing == "y":
        playing = True
        computer = t[randint(0,2)]
    else:
        playing = False
        print("Thanks for playing!")
        print("Your score was", score)
        break
    
