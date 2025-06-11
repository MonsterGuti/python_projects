from random import choice

options = ["rock", "paper", "scissors"]
your_choice = input("Choose rock, paper, or scissors: ")
computer_choice = choice(options)

print(f"Your choice: {your_choice}")
print(f"Computer choice: {computer_choice}")

if your_choice not in options:
    print("Invalid choice! Please choose rock, paper, or scissors.")
else:
    if your_choice == computer_choice:
        print("Draw!")
    elif (your_choice == "rock" and computer_choice == "scissors") or \
         (your_choice == "scissors" and computer_choice == "paper") or \
         (your_choice == "paper" and computer_choice == "rock"):
        print("You won!")
    else:
        print("You lost!")

