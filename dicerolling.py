import random

dice1 = [1, 2, 3, 4, 5, 6]
dice2 = [1, 2, 3, 4, 5, 6]

dicereal1 = random.choice(dice1)
dicereal2 = random.choice(dice2)

print(str(dicereal1) + ", " + str(dicereal2))

def rolldice():

    roll = input("D0 you want to roll dice?")

    while (roll == "yes"):
        dice1 = [1, 2, 3, 4, 5, 6]
        dice2 = [1, 2, 3, 4, 5, 6]

        dicereal1 = random.choice(dice1)
        dicereal2 = random.choice(dice2)

        print(str(dicereal1) + ", " + str(dicereal2))

        roll = input("D0 you want to roll dice?")


rolldice()

