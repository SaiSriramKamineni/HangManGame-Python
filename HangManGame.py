import random

def display_hangman(chances_left):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """
    ]
    return stages[chances_left]

# List of words for the Hangman game
words = [
    "python", "javascript", "hangman", "algorithm", "function",
    "variable", "syntax", "compiler", "interpreter", "debugging",
    "loop", "conditional", "exception", "inheritance", "encapsulation","rishitha"
]


# Choose a random word from the list
word = random.choice(words)

# Initialize the guessed word with underscores
guessed_word = ["_"] * len(word)

# Set the total number of chances
total_chances = 6

# Welcome message and initial game state
print("Welcome to Hangman Game")
print(f"You have {total_chances} chances to guess the word")
print(display_hangman(total_chances))
print(" ".join(guessed_word))

# Game loop
while total_chances > 0 and "".join(guessed_word)!= word:
    letter = input("Guess a letter: ").lower()

    if letter in word:
        # Update the guessed word with the correct letter
        for index in range(len(word)):
            if word[index] == letter:
                guessed_word[index] = letter
        print("Good guess!")
    else:
        # Decrement the number of chances if the guess is incorrect
        total_chances -= 1
        print("Incorrect guess")

    # Display the current state of the guessed word and remaining chances
    print(display_hangman(total_chances))
    print(" ".join(guessed_word))
    print(f"The remaining chances are: {total_chances}")

# Final game outcome
if "".join(guessed_word) == word:
    print("Congratulations! You have guessed the word correctly")
else:
    print("Game over")
    print("You lose. All the chances are exhausted")
    print(f"The word was: {word}")

# Additional features
print("\nWould you like to play again? (yes/no)")
response = input().lower()
if response == "yes":
    print("Let's play again!")
    # Reset the game state
    word = random.choice(words)
    guessed_word = ["_"] * len(word)
    total_chances = 6
    print("Welcome to Hangman Game")
    print(f"You have {total_chances} chances to guess the word")
    print(display_hangman(total_chances))
    print(" ".join(guessed_word))
    
    # Restart the game loop
    while total_chances > 0 and "".join(guessed_word)!= word:
        letter = input("Guess a letter: ").lower()

        if letter in word:
            # Update the guessed word with the correct letter
            for index in range(len(word)):
                if word[index] == letter:
                    guessed_word[index] = letter
            print("Good guess!")
        else:
            # Decrement the number of chances if the guess is incorrect
            total_chances -= 1
            print("Incorrect guess!!!")

        # Display the current state of the guessed word and remaining chances
        print(display_hangman(total_chances))
        print(" ".join(guessed_word))
        print(f"The remaining chances are: {total_chances}")

    # Final game outcome
    if "".join(guessed_word) == word:
        print("Congratulations! You have guessed the word correctly and saved the man's life!")
    else:
        print("Game over")
        print("You lose. All the chances are exhausted and couldn't able to save his life ")
        print(f"The word was: {word}")
else:
    print("Thanks for playing!")