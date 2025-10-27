import random

print(f"------NUMBER GUESSR-----\nThe objective of the game is to guess the correct number within SEVEN attempts. Good luck!")

upper_bound = int(input("Please enter the upper bound: "))
lower_bound = int(input("Please enter the lower bound: "))

number = random.randint(upper_bound, lower_bound)
tries_left = 7
guess_counter = 0

while tries_left >= guess_counter:
    guess_counter += 1
    guess = int(input("Enter your guess: "))

    if guess == number:
        print(f"Congratulations! The number was {number} and you guessed it in {guess_counter} attempts.")
        break
    
    elif guess > number:
        print(f"Too high! Go lower!")
    elif guess < number:
        print(f"Too low! Go higher!")
    elif guess_counter >= tries_left:
        print(f"Sorry, the number was {number}. Try again next time!")