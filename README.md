### What Is This Project?

This project is a Python-based version of the classic Hangman word guessing game, but with an added feature: a countdown timer for each guess. The timer adds pressure and excitement to the game and teaches how to manage timed input in Python.



### What the Game Does

* It selects a random word from a small list of fruit names.
* A hint related to the word is shown to the player.
* The player has to guess the word one letter at a time.
* Only six wrong guesses are allowed — just like traditional Hangman.
* Each guess must be made within 10 seconds. If the player takes too long, it counts as a wrong guess.



### How the Game Works (Step-by-Step)

#### 1. Setup and Modules

* The game uses Python's `random` module to randomly pick a word from the dictionary.
* It uses the `threading` module to create a countdown timer. The input function runs in one thread, while the timer runs in another.
* ASCII art is used to show the hangman figure being drawn step by step as the player makes incorrect guesses.

#### 2. Word and Hint System

* The game stores a small dictionary of words along with hints.
  For example:

  ```python
  "apple": "A red or green fruit"
  ```
* When a word is selected, its hint is displayed to help the player guess.

#### 3. Game Loop

* The game starts by showing the hint and blank spaces for the letters in the word (like `_ _ _ _ _`).
* The player types one letter at a time to guess the word.
* If the guess is correct, the letter is filled in at the right positions.
* If the guess is wrong or takes too long, a part of the hangman drawing is shown, and the player loses one of the six allowed attempts.

#### 4. Timer Logic

* For every guess, the program waits for input using a separate thread.
* If the player enters a guess within 10 seconds, the game continues.
* If the time runs out, the game notifies the player and deducts an attempt.
* This feature adds urgency and helps you learn how to handle real-time input using threads in Python.

#### 5. End of Game

* The game ends in two situations:

  * The player successfully guesses all the letters in the word.
  * The player uses up all six attempts.
* After the game, the final score is shown, and the player is asked if they want to play again.



### What I Learned from This Project

This project helped me apply and understand several important Python concepts:

* Working with functions and loops
* Using dictionaries to store data like words and hints
* Handling user input efficiently
* Creating a modular program by breaking it into smaller functions
* Most importantly, using **threads** to manage time-based actions, which is useful for building real-time or interactive applications



### Real-Life Applications of This Code

The concepts used in this project can be adapted for:

* Timed quizzes or tests
* Command-line tools with countdowns
* Educational games for children
* Any scenario that requires a response within a time limit



### Final Summary You Can Use

This Hangman game is a fun and educational project that allowed me to practice Python fundamentals while also learning more advanced topics like multithreading and input control. It not only strengthens logical thinking but also shows how to build user-interactive programs that respond to time-sensitive events. These skills are valuable for both gaming applications and real-world software development.
