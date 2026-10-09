import random

WORDS = ["python", "internship", "computer", "keyboard", "program"]
MAX_WRONG = 6


def display_word(word, guessed):
    """Show the word with underscores for letters not yet guessed."""
    return " ".join(letter if letter in guessed else "_" for letter in word)


def play():
    word = random.choice(WORDS)
    guessed = []
    wrong = 0

    print("=== HANGMAN ===")
    print(f"Guess the word one letter at a time. You can make {MAX_WRONG} wrong guesses.\n")

    while wrong < MAX_WRONG:
        print("Word:", display_word(word, guessed))
        print(f"Wrong guesses left: {MAX_WRONG - wrong}")
        print("Guessed letters:", " ".join(sorted(guessed)) if guessed else "none")

        guess = input("Enter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        if guess in guessed:
            print("You already guessed that letter.\n")
            continue

        guessed.append(guess)

        if guess in word:
            print("Correct!\n")
        else:
            wrong += 1
            print("Wrong!\n")

        if all(letter in guessed for letter in word):
            print(f"You won! The word was '{word}'.")
            return

    print(f"Game over! The word was '{word}'.")


def main():
    while True:
        play()
        again = input("\nPlay again? (y/n): ").lower().strip()
        if again != "y":
            print("Thanks for playing!")
            break
        print()


if __name__ == "__main__":
    main()