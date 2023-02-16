import random

def get_choices():
    player_choice = input("Enter a choice: rock, paper, scissors: ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}

    return choices

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer: 
        return "its a tie"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win"
        else:
            return "Rock looses to paper! You loose"
    elif player == "paper":
        if computer == "scissors":
            return "Paper looses to scissors. You loose"
        else:
            return "Paper covers rock. You win"
    elif player == "scissors":
        if computer == "paper":
            return "scissors cuts paper! You win"
        else:
            return "scissors looses to rock! You loose"
    

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
