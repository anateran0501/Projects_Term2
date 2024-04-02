import random

def guess_the_number():
    number_to_guess = random.randint(0, 9999)
    attempts = 5
    
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 0 and 9999.")
    print("You have 5 chances to guess the number.")

    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))
        
        if guess == number_to_guess:
            print(f"Congratulations! You've guessed the number in {attempt} attempts!")
            break
        else:
            if abs(guess - number_to_guess) > 1000:
                print("You're far from the number.")
            elif abs(guess - number_to_guess) > 100:
                print("You're close, but not quite there.")
            else:
                print("You're very close!")
                
        if attempt == attempts:
            print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")

if __name__ == "__main__":
    guess_the_number()
