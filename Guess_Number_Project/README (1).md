**Number Guessing Game**






**Overview**





This is a simple Python program that generates a random number between 1 and 100 and allows the user to guess the number within 3 attempts. The program provides hints if the guessed number is too high or too low.






**How It Works**





The program generates a random number using Python's random.randint(1, 100) function.







The user is prompted to guess the number.






If the guess is higher than the generated number, the program suggests guessing a lower number.






If the guess is lower, the program suggests guessing a higher number.






The user has a maximum of 3 attempts to guess correctly.





If the user guesses correctly within the given attempts, they win.






If the user fails to guess correctly within 3 attempts, the program reveals the correct number.




How to Run the Program




Ensure you have Python installed on your system.




Copy the script into a .py file, for example, guess_game.py.




Open a terminal or command prompt and navigate to the file's location.





Run the script using the command:




    python guess_game.py



    

Follow the on-screen instructions to play the game.







**Example Output**

    Guess the number between 1 and 100! (Max attempts: 3)
    Enter your guess: 50
    Lower number please
    Enter your guess: 25
    Higher number please
    Enter your guess: 30
    Congratulations! You guessed the number 30 correctly in 3 attempts.

**OR**

    Guess the number between 1 and 100! (Max attempts: 3)
    Enter your guess: 80
    Lower number please
    Enter your guess: 40
    Higher number please
    Enter your guess: 50
    Sorry! You've used all 3 attempts. The correct number was 55.





Requirements





Python 3.x




Features





Random number generation





Input validation (ensuring user enters an integer)





Hints to guide the user






Limited attempts for an added challenge






Possible Enhancements






Allowing the user to choose difficulty levels (e.g., more attempts for easier mode)






Adding a replay option






Providing a scoring system based on attempts used







Enjoy the game! 🎮

