# # Create a simple number guessing game in Python.
import random


def input_number():
    try:
        user_input = int(input("Enter your guess: "))
        return user_input
    except ValueError:
        print("Invalid input")
        return input_number()
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    no_of_attempts = 0
    secret_number = random.randint(1, 100)
    while True:
        user_guess = input_number()
        no_of_attempts += 1
        if user_guess == secret_number:
            print(
                f"Congratulations! You guessed the number in {no_of_attempts} attempts."
            )
            break
        elif user_guess < secret_number:
            print("Too low. Try again.")
        elif user_guess > secret_number:
            print("Too high. Try again.")


if __name__ == "__main__":
    main()
    print("Thank you for playing!")
