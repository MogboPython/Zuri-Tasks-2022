import random

options = {"R": "Rock", "P": "Paper", "S":"Scissors"}


def rps_game(player, cpu):

    print("Player(%s) : CPU(%s)" %(options[player], options[cpu]))

    if player == cpu:
        print("It is a tie. Rematch! \n")
        start()
    
    elif (player == "R" and cpu == "S") or (player == "P" and cpu == "R") or (player == "S" and cpu == "P"):
        print("Player Wins")

    elif (cpu == "R" and player == "S") or (cpu == "P" and player == "R") or (cpu == "S" and player == "P"):
        print("CPU Wins")


def start():
    cpu_pick = random.choice(list(options))
    player_pick = input("Enter R for Rock, P for Paper or S for Scissors: ")

    while player_pick not in options.keys():
        player_pick = input("Error, Enter R for Rock, P for Paper or S for Scissors: ")

    rps_game(player_pick, cpu_pick)

    
start()

