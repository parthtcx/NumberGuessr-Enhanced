import random

print(f"------NUMBER GUESSR-----\nThe objective of the game is to guess the correct number within a range. Good luck!")

# Difficulty Config
difficulty = int(input("Please choose a difficulty level!\n1. Easy -- 10 Tries\n2. Medium -- 7 Tries\n3. Hard -- 5 Tries\n4. Expert -- 3 Tries\nSelect (1-4): "))

if difficulty == 1:
    difficulty_name = "Easy"
    tries_left = 10
elif difficulty == 2:
    difficulty_name = "Medium"
    tries_left = 7
elif difficulty == 3:
    difficulty_name = "Hard"
    tries_left = 5
elif difficulty == 4:
    difficulty_name = "Expert"
    tries_left = 3
else:
    tries_left = 7
    difficulty_name = "Medium"
    print(f"Invalid input! Defaulting to Medium difficulty!")

print(f"You have selected {difficulty_name} and have {tries_left} attempts to guess the number.")

lower_bound = int(input("Please enter the lower bound: "))
upper_bound = int(input("Please enter the upper bound: "))

number = random.randint(lower_bound, upper_bound)
guess_counter = 0

while tries_left > guess_counter:
    remaining_attempts = tries_left - guess_counter
    guess = int(input(f"Enter your guess ({remaining_attempts} attempts left): "))
    guess_counter += 1
    
    if guess == number:
        print(f"Congratulations! The number was {number} and you guessed it in {guess_counter} tries.")
        break
    elif guess_counter >= tries_left:
        print(f"Sorry, the number was {number}. Try again next time!")
    elif guess > number:
        print(f"Too high! Go lower!")
    elif guess < number:
        print(f"Too low! Go higher!")
