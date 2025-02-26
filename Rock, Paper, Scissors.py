import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("""Type Rock/Paper/Scissors or Q to quit: 
""").lower()
    if user_input == "q":
        print(f"User: {user_wins} - Computer: {computer_wins}")
        if computer_wins > user_wins:
            print("Computer wins!")
        else:
            print("You win!")
        break

    if user_input not in ["rock", "paper", "scissors"]:
        print("Please input a valid selection")
        continue

    random_number = random.randint(0,2)
    # rock : 0, paper : 1, scissors: 2
    computer_pick = options[random_number]
    print(f"Computer picked {computer_pick}.")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
        continue
    if user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
        continue
    if user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
        continue
    else:
        print("You lost. Try again.")
        computer_wins += 1


print("Goodbye!")