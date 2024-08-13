import random

def guess_the_number():
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")

    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    number_of_tries = 0
    guessed_correctly = False

    while not guessed_correctly:
        # Prompt the player to enter a guess
        try:
            guess = int(input("Take a guess: "))
        except ValueError:
            print("Please enter a valid number.")

        number_of_tries += 1

        # Check the player's guess
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            guessed_correctly = True
            print(f"Congratulations! You guessed the number in {number_of_tries} tries.")

if __name__ == "__main__":
    guess_the_number()
