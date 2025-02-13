import random

categories = {
    "ANIMAL" :['PENGUIN', 'ALIGATOR', 'WOLF', 'PARROT', 'SNAKE', 'TIGER', 'BEAR'],
    "COUNTRY" :['PERU', 'SPAIN', 'JAPAN', 'CANADA', 'GERMANY', 'AUSTRALIA', 'AFGANISTAN'],
    "COLOR" :['WHITE', 'BLACK', 'MAGENTA', 'VIOLET', 'GREEN', 'YELLOW', 'INDIGO'],
    "FRUIT" :['BLACKBERRY', 'CANTALOUPE', 'CLEMENTINE', 'WATERMELON', 'HONEYDEW', 'STRAWBERRY', 'NECTARINE'],
    "SPORT" :['BASKETBALL', 'HOCKEY', 'TENNIS', 'BADMINTON', 'LACROSSE', 'WRESTLING']
}

# Choose the category
def choose_category(categories):
    while True:
        choice = input("Please choose your category: Animal, Country, Color, Fruit, Sport: ").upper()
        if choice in categories:
            return choice
        else:
            print("Invalid category! Please choose again.")

# Get the secret word from the selected category
def get_secret_word(choice):
    return random.choice(categories[choice])

# Player makes a guess
def player_guess(secret_word):
    while True:
        guess = input("Enter your letter or guess the word: ").strip().upper()
        if len(guess) == 1 and guess.isalpha():
            return guess
        elif len(guess) == len(secret_word) and guess.isalpha():
            return guess
        else:
            print("Guess must be single letters!")

# Check if the guessed letter or word is in the secret word
def checking(guess, secret_word, reveal):
    if guess == secret_word:
        return secret_word, True

    word_reveal = ""
    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            word_reveal += guess
        else:
            word_reveal += reveal[i]

    return word_reveal, False

# Display the game state, including the current hangman stage
def display_game(reveal, guessed_letters, choice, incorrect):
    empty_space = " ".join(reveal)
    print(f"Category: {choice}")
    print(f"Word: {empty_space}")
    print(f"Guessed letters: {guessed_letters}")
    print(display_hangman(incorrect))

# Hangman visual representation
def display_hangman(incorrect):
    stages = [
        """
         -----
         |   |
             |
             |
             |
             |
        =======
        """,
        """
         -----
         |   |
         O   |
             |
             |
             |
        =======
        """,
        """
         -----
         |   |
         O   |
         |   |
             |
             |
        =======
        """,
        """
         -----
         |   |
         O   |
        /|   |
             |
             |
        =======
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
             |
             |
        =======
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
        /    |
             |
        =======
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
        / \\  |
             |
        =======
        """
    ]
    return stages[incorrect]

# Main hangman game function
def hangman():
    print("WELCOME TO HANGMAN!")
    choice = choose_category(categories)
    secret_word = get_secret_word(choice)
    incorrect = 0
    max_incorrect = 7
    guessed_letters = ""
    reveal = "_" * len(secret_word)

    while incorrect < max_incorrect:
        display_game(reveal, guessed_letters, choice, incorrect)
        guess = player_guess(secret_word)

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters += guess

        reveal, correct_guess = checking(guess, secret_word, reveal)

        if guess not in secret_word:
            incorrect += 1
            print(f"Woah oh! You have {max_incorrect - incorrect} tries left!")

        if correct_guess or "_" not in reveal:
            print(f"Congrats! You got the hidden word {secret_word}!")
            break

    if incorrect == max_incorrect:
        print(f"Outta guesses! The hidden word was {secret_word}")

    retry = input("Do you wish to play again? Yes or no: ").strip().upper()
    if retry == "YES":
        hangman()
    else:
        print("Thank you for playing!")

if __name__ == "__main__":
    hangman()


