import random

# Define a class for the Guessing Word game
class GuessingWord:
    def __init__(self, words_with_hints, max_attempts):
        self.words_with_hints = words_with_hints  # Dictionary of words and their hints
        self.word = ""  # The selected word to guess
        self.hint = ""  # Hint associated with the selected word
        self.max_attempts = max_attempts  # Maximum number of incorrect attempts allowed

    def select_word(self):
        # Randomly choose a word and its hint from the dictionary
        items = list(self.words_with_hints.items())
        random_choice = random.choice(items)
        self.word = random_choice[0]  # Selected word
        self.hint = random_choice[1]  # Associated hint

    def play_game(self):
        print("Welcome to the 'Guess the Word' Game!")
        print("Hints will guide you, and you have limited attempts.")
        
        self.select_word()  # Select a random word and hint

        guessed_word = ["_"] * len(self.word)  # Placeholder for the word
        attempts = self.max_attempts  # Initialize attempts counter
        used_letters = []  # Track used letters

        print(f"\nHint: {self.hint}")  # Display the hint

        # Main game loop
        while attempts > 0:
            # Display current progress and game status
            print(f"\nCurrent word: {' '.join(guessed_word)}")
            print(f"Attempts left: {attempts}")
            print(f"Used letters: {', '.join(used_letters)}")

            # Get user input
            guess = input("Enter a letter or the full word: ").lower()

            if len(guess) == 1:  # If the input is a single letter
                if guess in used_letters:
                    print("You've already used this letter. Try again.")
                elif guess in self.word:
                    print(f"Good job! '{guess}' is in the word.")
                    used_letters.append(guess)  # Add to used letters
                    # Update the guessed word with the correct letter
                    for index in range(len(self.word)):
                        if self.word[index] == guess:
                            guessed_word[index] = guess
                else:
                    print(f"'{guess}' is not in the word. Try again.")
                    attempts -= 1  # Decrease attempts for incorrect guess
                    used_letters.append(guess)

            elif guess == self.word:  # If the user guesses the full word correctly
                print(f"Congratulations! You guessed the word: {self.word}")
                return
            else:
                print("Incorrect guess. Try again.")
                attempts -= 1  # Decrease attempts for incorrect full word guess

            # Check if the word has been completely guessed
            if "_" not in guessed_word:
                print(f"Congratulations! You guessed the word: {self.word}")
                return

        # If attempts run out, reveal the correct word
        print(f"\nOut of attempts! The correct word was: {self.word}. Better luck next time!")

# Words with hints dictionary
words_with_hints = {
    "earth": "The third planet from the sun, our home.",
    "ocean": "A large body of saltwater covering most of the Earth's surface.",
    "computer": "An electronic device used to process data.",
    # Add more words and hints as needed
}

# Define the maximum number of attempts
max_attempts = 3

# Create an instance of the GuessingWord class and start the game
game = GuessingWord(words_with_hints, max_attempts)
game.play_game()
