import random

list = ["R","P","S"]

keep_playing = "true" #This is a switch for the game, as this loop stays forever

while keep_playing == "true":
    CPU = random.choice(list)
    Player = input("Pick your option: 'R','P' or 'S'")
    print("CPU:",CPU)

    if CPU == Player:
        print("Tie")
    elif Player == "R" and CPU == "S":
        print("Player Wins!")
    elif Player == "R" and CPU == "P":
        print("Computer Wins!")
    elif Player == "P" and CPU == "R":
        print("Player Wins!")
    elif Player == "P" and CPU == "S":
        print("Computer Wins!")
    elif Player == "S" and CPU == "P":
        print("Player Wins!")
    elif Player == "S" and CPU == "R":
        print("Computer Wins!")

while Player not in list:
    print("Error: Invalid. Please, choose 'R','P' or 'S'")


