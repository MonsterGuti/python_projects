from random import randint

while True:
    level = input("Choose difficulty (easy, medium or hard): ")

    if level == "easy":
        computer_choice = randint(1, 100)
        max_range = 100
        print("The number you have to guess is between 1 and 100!")
    elif level == "medium":
        computer_choice = randint(1, 200)
        max_range = 200
        print("The number you have to guess is between 1 and 200!")
    elif level == "hard":
        computer_choice = randint(1, 500)
        max_range = 500
        print("The number you have to guess is between 1 and 500!")
    else:
        print("Invalid difficulty level. Try again!")
        continue

    print("Good luck!")

    while True:
        user_input = input(f"Enter a number between 1 and {max_range}: ")

        if not user_input.isdigit():
            print("Invalid input. Please enter a valid number.")
            continue

        user_number = int(user_input)

        if user_number < 1 or user_number > max_range:
            print(f"Out of range! Please enter a number between 1 and {max_range}.")
        elif user_number < computer_choice - 10:
            print("Too low!")
        elif user_number < computer_choice:
            print("It is a bit higher! You are very close!")
        elif user_number > computer_choice + 10:
            print("Too high!")
        elif user_number > computer_choice:
            print("It is a bit lower! You are very close!")
        else:
            print("You guessed it!")
            break

    response = input("Do you want to play again? y/n: ")
    if response.lower() == "n":
        print("Goodbye!")
        break
