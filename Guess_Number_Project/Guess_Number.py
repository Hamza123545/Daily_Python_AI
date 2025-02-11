import random

n = random.randint(1, 100)

print("Guess the number between 1 and 100! (Max attempts: 3)")

for guesses in range(1, 4):  
    a = int(input("Enter your guess: "))

    if a > n:
        print("Lower number please")
    elif a < n:
        print("Higher number please")
    else:
        print(f"Congratulations! You guessed the number {n} correctly in {guesses} attempts.")
        break
else:
    print(f"Sorry! You've used all 3 attempts. The correct number was {n}.")
