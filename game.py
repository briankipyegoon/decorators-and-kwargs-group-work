import random

def score_tracker(func):
    score = 0  # Initialize score within the decorator

    def wrapper(args, **kwargs):
        nonlocal score  # Allow the inner function to modify the outer score variable
        result = func(args, **kwargs)  # Call the original function
        if result:  # If the guess was correct
            score +=10  # Add points
        print(f"Your current score is: {score}")  # Print the current score
        return result  # Return the result of the function
    return wrapper

@score_tracker
def guess_number(player_guess):
    random_number = random.randint(1, 10)  # Generate a random number
    print(f"The random number is: {random_number}")  # Debugging aid
    if player_guess == random_number:
        print("Correct guess! ")
        return True  # Indicate a correct guess
    else:
        print("Wrong guess. Try again!")
        return False  # Indicate an incorrect guess




  #Test the program
print("Welcome to the Guessing Game! ")
for attempt in range(1,101):  # Allow the player to guess 100 times
        try:
            guess = int(input(f"Attempt {attempt + 1}/3 - Enter your guess (1-10): "))
            if guess < 1 or guess > 10:
                print("Please guess a number between 1 and 10!")
                continue
            guess_number(guess)  # Call the decorated function
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 10")


