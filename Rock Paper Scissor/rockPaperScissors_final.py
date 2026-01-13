# Create a simple rock paper scissors game in Python.

# ASCII art for the game:
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Dictionary to map the user/computer choice to the ASCII art
ascii_art = {
    "rock": rock,
    "paper": paper,
    "scissors": scissors,
}


def get_user_choice():
    while True:
        get_user_choice = (
            input("Enter your choice: rock, paper, scissors: ").lower().strip()
        )
        if get_user_choice in ascii_art:
            return get_user_choice, ascii_art[get_user_choice]
        else:
            print(
                "Invalid choice. Please try again. Enter your choice: rock, paper, scissors: "
            )


def get_computer_choice():
    choices = list(ascii_art.keys())
    computer_choice = random.choice(choices)
    return computer_choice, ascii_art[computer_choice]


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Your chose:", user_choice)
        print(ascii_art[user_choice])
        print("Computer chose:", computer_choice)
        print(ascii_art[computer_choice])
        return "It's a Tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("Your chose:", user_choice)
        print(ascii_art[user_choice])
        print("Computer chose:", computer_choice)
        print(ascii_art[computer_choice])
        return "You win!"
    else:
        print("Your chose:", user_choice)
        print(ascii_art[user_choice])
        print("Computer chose:", computer_choice)
        print(ascii_art[computer_choice])
        return "Computer wins!"


def start_game():
    flag = True
    while flag:
        print("Welcome to Rock Paper Scissor!")
        user_choice, user_art = get_user_choice()
        computer_choice, computer_art = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        print(result)
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thank you for playing Rock Paper Scissor!")
            flag = False


if __name__ == "__main__":
    import random

    start_game()
