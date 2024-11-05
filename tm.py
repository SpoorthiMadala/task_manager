import numpy as np

def game():
    
    target = np.random.randint(1, 101)
    attempts = 5
    won = False

    

    while attempts > 0:
        try:
            
            guess = int(input("Guess the number (between 1 and 100): "))

            
            if guess < 1 or guess > 100:
                print("Invalid number. Please enter a number between 1 and 100.")
                continue

            
            if guess == target:
                print("Congratulations! You guessed the correct number!")
                won = True
                break
            elif guess > target:
                print("Your guess is too high.")
            else:
                print("Your guess is too low.")
                
            
            attempts -= 1
            if attempts > 0:
                print(f"You have {attempts} attempts left. Try again.")
            else:
                print("No attempts left.")
                
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    if not won:
        print(f"Sorry, you've lost. The correct number was {target}.")
    
    return won


score = 0
attempts=5
print("\nWelcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 100.")
print(f"You have {attempts} attempts to guess it correctly.\n")

while True:
    if game():
        score += 1
    
    
    choice = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if choice == "no":
        print(f"\nThank you for playing! Your final score is {score}.")
        break
