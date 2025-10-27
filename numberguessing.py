import random

# Color Codes
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m' 

# ASCII ART
WIN_ART = f"""{Colors.GREEN}
  ★ ☆ ★  W I N N E R !  ★ ☆ ★
    ╔══════════════════════╗
    │  CONGRATULATIONS!    │
    │   You guessed it!    │
    ╚══════════════════════╝
       ✨ 🎉 🎊 ✨
{Colors.END}"""

LOSE_ART = f"""{Colors.RED}
  ☠  G A M E  O V E R  ☠
    ╔══════════════════════╗
    │     Better luck      │
    │      next time!      │
    ╚══════════════════════╝
       💀 😞 💀
{Colors.END}"""

# Streak counters
current_streak = 0
best_streak = 0

def play_game():
    global current_streak, best_streak
    
    print(f"{Colors.CYAN}{Colors.BOLD}-----NUMBER GUESSR-----{Colors.END}")
    print(f"{Colors.WHITE}The objective is to guess the correct number within a range. Good luck!{Colors.END}")

    # Streak Display
    if current_streak > 0:
        print(f"{Colors.YELLOW}Current Win Streak: {current_streak} | Best Streak: {best_streak}{Colors.END}")
    print()

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
        print(f"{Colors.YELLOW}Invalid input! Defaulting to Medium difficulty!{Colors.END}")

    print(f"{Colors.BLUE}You have selected {difficulty_name} and have {tries_left} attempts to guess the number.{Colors.END}")

    lower_bound = int(input(f"{Colors.WHITE}Please enter the lower bound: {Colors.END}"))
    upper_bound = int(input(f"{Colors.WHITE}Please enter the upper bound: {Colors.END}"))

    number = random.randint(lower_bound, upper_bound)
    guess_counter = 0
    won = False
    previous_guess = []

    while guess_counter < tries_left:
        remaining_attempts = tries_left - guess_counter
        guess = int(input(f"Enter your guess ({remaining_attempts} attempts left): "))
        guess_counter += 1
        previous_guess.append(guess)
        
        if guess == number:
            print(WIN_ART)
            print(f"{Colors.GREEN}Congratulations! The number was {number} and you guessed it in {guess_counter} attempts.{Colors.END}")
            current_streak += 1
            if current_streak > best_streak:
                best_streak = current_streak
            won = True
            
            # Streak Milestone
            if current_streak == 3:
                print(f"{Colors.PURPLE}You're on fire! 3 wins in a row!{Colors.END}")
            elif current_streak == 5:
                print(f"{Colors.PURPLE}Unstoppable! 5 IN A ROW!{Colors.END}")
            elif current_streak == 10:
                print(f"{Colors.PURPLE}LEGENDARY! 10-win streak!{Colors.END}")
            break

        elif guess > number:
            print(f"{Colors.RED}Too high! Go lower!{Colors.END}")
        elif guess < number:
            print(f"{Colors.RED}Too low! Go higher!{Colors.END}")

        # Hint Config
        if guess != number and hint_level != "none":
            if guess_counter == 2 and hint_level in ["generous", "moderate"]:
                mid_point = (upper_bound + lower_bound) // 2
                if number < mid_point:
                    print(f"{Colors.YELLOW}HINT: The number is in the lower half of the range.{Colors.END}")
                else:
                    print(f"{Colors.YELLOW}HINT: The number is in the upper half of the range.{Colors.END}")
            
            elif guess_counter == 4 and hint_level == "generous":
                if number % 2 == 0:
                    print(f"{Colors.YELLOW}HINT: Number is even!{Colors.END}")
                else:
                    print(f"{Colors.YELLOW}HINT: Number is odd!{Colors.END}")
            
            elif remaining_attempts == 1 and hint_level == "generous":
                close_range_low = max(lower_bound, number - 5)
                close_range_high = min(upper_bound, number + 5)
                print(f"{Colors.YELLOW}FINAL HINT: The number is between {close_range_low} and {close_range_high}!{Colors.END}")

        # Show previous guesses
        if hint_level != "none" and guess != number:
            print(f"{Colors.CYAN}Previous guesses: {previous_guess}{Colors.END}")

        # Check if lost on last attempt
        if guess_counter >= tries_left and not won:
            print(LOSE_ART)
            print(f"{Colors.RED}Sorry, the number was {number}. Try again next time!{Colors.END}")
            current_streak = 0

# Main game loop
while True:
    play_game()
    
    play_again = input(f"\n{Colors.WHITE}Play again? (y/n): {Colors.END}").lower()
    if play_again not in ['y', 'yes']:
        print(f"{Colors.CYAN}Thanks for playing! Final stats - Current Streak: {current_streak} | Best Streak: {best_streak}{Colors.END}")
        break
    print("\n" + "="*50 + "\n")