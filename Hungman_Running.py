import random
import threading
import sys
import time


# Word bank with hints
WORDS = {
    "apple": "A red or green fruit",
    "banana": "A long yellow fruit",
    "grape": "Small round fruit, often purple or green",
    "mango": "A tropical stone fruit",
    "orange": "A citrus fruit and also a color"
}

TIME_LIMIT = 10  # seconds for each guess


def get_display_word(word, guessed):
    return " ".join([letter if letter in guessed else "_" for letter in word])


def timed_input(prompt, timeout):
    guess = [None]

    def read_input():
        guess[0] = input(prompt).strip().lower()

    thread = threading.Thread(target=read_input)
    thread.start()
    thread.join(timeout)

    if thread.is_alive():
        print("\n⌛ Time's up!")
        return None
    return guess[0]


def get_valid_input(prompt, guessed):
    while True:
        guess = timed_input(f"{prompt} (⏳ {TIME_LIMIT}s): ", TIME_LIMIT)
        if guess is None:
            return None
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Enter a single letter (A-Z).")
        elif guess in guessed:
            print("🔁 You already guessed that.")
        else:
            return guess


def play_hangman():
    word, hint = random.choice(list(WORDS.items()))
    guessed = []
    attempts = 6

    print("\n🎮 Welcome to Hangman!")
    print(f"💡 Hint: {hint}")
    print(HANGMAN_PICS[0])
    print(get_display_word(word, guessed))

    while attempts > 0:
        guess = get_valid_input("🔤 Guess a letter", guessed)

        if guess is None:
            print("❌ Missed turn due to timeout.")
            attempts -= 1
        else:
            guessed.append(guess)
            if guess in word:
                print("✅ Correct!")
            else:
                attempts -= 1
                print(f"❌ Wrong! {attempts} attempts left.")

        print(HANGMAN_PICS[6 - attempts])
        display_word = get_display_word(word, guessed)
        print(display_word)

        if "_" not in display_word:
            print("🎉 You won! The word was:", word)
            return True

    print("💀 You lost! The word was:", word)
    return False


def main():
    score = 0
    while True:
        result = play_hangman()
        if result:
            score += 1
        print(f"🏆 Current Score: {score}")
        again = input("🔁 Play again? (y/n): ").lower()
        if again != "y":
            print("👋 Thanks for playing! Final Score:", score)
            break


main()
