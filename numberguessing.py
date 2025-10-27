import random

# ASCII ART
# ASCII Art
WIN_ART = """
  ★ ☆ ★  W I N N E R !  ★ ☆ ★
    ╔══════════════════════╗
    │  CONGRATULATIONS!    │
    │   You guessed it!    │
    ╚══════════════════════╝
       ✨ 🎉 🎊 ✨
"""

LOSE_ART = """
  ☠  G A M E  O V E R  ☠
    ╔══════════════════════╗
    │     Better luck      │
    │      next time!      │
    ╚══════════════════════╝
       💀 😞 💀
"""

print(f"------NUMBER GUESSR-----\nThe objective of the game is to guess the correct number within a range. Good luck!")

# Difficulty Config
difficulty = int(input("Please choose a difficulty level!\n1. Easy -- 10 Tries\n2. Medium -- 7 Tries\n3. Hard -- 5 Tries\n4. Expert -- 3 Tries\nSelect (1-4): "))

if difficulty == 1:
    difficulty_name = "Easy"
    tries_left = 10
    hint_level = "generous"
elif difficulty == 2:
    difficulty_name = "Medium"
    tries_left = 7
    hint_level = "moderate"
elif difficulty == 3:
    difficulty_name = "Hard"
    tries_left = 5
    hint_level = "minimal"
elif difficulty == 4:
    difficulty_name = "Expert"
    tries_left = 3
    hint_level = "none"
else:
    tries_left = 7
    difficulty_name = "Medium"
    hint_level = "moderate"
    print(f"Invalid input! Defaulting to Medium difficulty!")

print(f"You have selected {difficulty_name} and have {tries_left} attempts to guess the number.")


lower_bound = int(input("Please enter the lower bound: "))
upper_bound = int(input("Please enter the upper bound: "))

number = random.randint(lower_bound, upper_bound)
guess_counter = 0
previous_guess = []

while tries_left > guess_counter:
    remaining_attempts = tries_left - guess_counter
    guess = int(input(f"Enter your guess ({remaining_attempts} attempts left): "))
    guess_counter += 1
    previous_guess.append(guess)
    
    if guess == number:
        print(WIN_ART)
        print(f"Congratulations! The number was {number} and you guessed it in {guess_counter} attempts.")
        break

    elif guess_counter >= tries_left:
        print(LOSE_ART)
        print(f"Sorry, the number was {number}. Try again next time!")

    elif guess > number:
        print(f"Too high! Go lower!")

    elif guess < number:
        print(f"Too low! Go higher!")

    # Hint Config
    if guess != number and hint_level!= "none":
        if guess_counter == 2 and hint_level in ["generous", "moderate"]:
            range_hint = upper_bound - lower_bound
            mid_point = (upper_bound + lower_bound) // 2
            if number < mid_point:
                print(f"HINT: The number is in the lower half of the range.")
            else:
                print(f"HINT: The number is in the upper half of the range.")
        

        elif guess_counter == 4 and hint_level == "generous":
            if number % 2 == 0:
                print("HINT: Number is even!")
            else:
                print("HINT: Number is odd!")
        
        elif remaining_attempts == 1 and hint_level == "generous":
            close_range_low = max(lower_bound, number - 5)
            close_range_high = max(upper_bound, number + 5)
            print(f"FINAL HINT: The number is in between {close_range_low} and {close_range_high}!")

    # Show previous guesses (all difficulties except Expert)
    if hint_level != "none" and guess!= number:
        print(f"Previous guesses: {previous_guess}")