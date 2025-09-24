#make a number guessing game in 10 guesses or less

import random

def guessing_game():
    number_to_guess = random.randint(1, 1000) #random number between 1 and 1000
    number_of_guesses = 0
    guessed = False #flag to check if the number is guessed
    print("Welcome to the Number Guessing Game!")
    print("A random number between 1 and 1000 has been generated, can you guess it?")

    while not guessed:
        try:
            user_guess = int(input("Enter your guess: ")) # prompt the user into making a guess
            number_of_guesses += 1 #increment the number of guesses
            if user_guess < 1 or user_guess > 1000:
                print("Please guess a number between 1 and 1000.")
                continue
            if user_guess < number_to_guess: #check if the guess is too low
                print("Too low! Try again.")
            elif user_guess > number_to_guess: #check if the guess is too high
                print("Too high! Try again.")
            else:
                guessed = True
                print(f"Congratulations! You've guessed the number {number_to_guess} in {number_of_guesses} guesses.")
            if number_of_guesses >= 10 and not guessed:
                print(f"Sorry, you've used all 10 guesses. The number was {number_to_guess}. Better luck next time!")
                break
        except ValueError: #handle non-integer inputs
            print("Invalid input. Please enter a valid integer.")
if __name__ == "__main__": #run the game
    guessing_game()

# replay the game if not guessed in 10 tries
    while True:
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again == 'yes':
            guessing_game()
        elif play_again == 'no':
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


