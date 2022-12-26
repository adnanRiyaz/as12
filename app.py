import random

while True:
    myans = input("Choose : rock,paper or scissor?")
    myans = myans.lower()

    if myans != "rock" and myans != "paper" and myans != "scissor":
        print("Please choose a correct answer.")
        continue
    compans = random.choice(["rock","paper","scissor"])
    if myans == compans:
        print(f"Computer Chose :{compans}")
        print("Game Tied !")
        continue
    elif myans =="rock" and compans =="scissor":
        print(f"Computer Chose :{compans}")
        print("You Win !")
        break
    elif myans =="paper" and compans == "rock":
        print(f"Computer Chose :{compans}")
        print("You Win !")
        break
    elif myans == "scissor" and compans =="paper":
        print(f"Computer Chose :{compans}")
        print("You Win !")
        break
    
    else:
        print(f"Computer Chose :{compans}")
        print("You Lose !")
        break