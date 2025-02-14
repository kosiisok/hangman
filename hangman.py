import random
# Sort words into categories
categories = {
    "ANIMAL" :['PENGUIN', 'ALIGATOR', 'WOLF', 'PARROT', 'SNAKE', 'TIGER', 'BEAR', 'CARDINAL', 'CHEETAH', 'GORILLA'],
    "COUNTRY" :['PERU', 'SPAIN', 'JAPAN', 'CANADA', 'GERMANY', 'AUSTRALIA', 'BAHAMAS', 'JAMACIA', 'ITALY', 'GREECE'],
    "COLOR" :['WHITE', 'BLACK', 'MAGENTA', 'VIOLET', 'GREEN', 'YELLOW', 'INDIGO', 'ORANGE', 'AQUAMARINE', 'MAROON'],
    "FRUIT" :['BLACKBERRY', 'CANTALOUPE', 'CLEMENTINE', 'WATERMELON', 'HONEYDEW', 'STRAWBERRY', 'NECTARINE', 'APRICOT', 'CRANBERRY', 'PINEAPPLE'],
    "SPORT" :['BASKETBALL', 'HOCKEY', 'TENNIS', 'BADMINTON', 'LACROSSE', 'WRESTLING', 'SOCCER', 'VOLLEYBALL', 'BASEBALL']
}

# Determines the category chosen for the game
def choose_category(categories):
    while True:
        #Asking player for what category they want
        choice = input("Please choose your category: Animal, Country, Color, Fruit, Sport: ").upper()
        if choice in categories:
            return choice
        #If they don't choose a category from the given choices then this will be prompted
        else:
            print("Invalid category! Please choose again.")

# Get the secret word from the selected category
def get_secret_word(choice):
    return random.choice(categories[choice])

# Player makes a guess
def player_guess(secret_word):
    while True:
        guess = input("Enter your letter or guess the word: ").strip().upper()
        #If guess is 1 letter it will be returned
        if len(guess) == 1 and guess.isalpha():
            return guess
            #If guess is the same length as the secret word but wrong it will be returned
        elif len(guess) == len(secret_word) and guess.isalpha():
            return guess
        #If anything else besides 1 letter or same length as the secret word this will be prompted
        else:
            print("Guess must be single letters!")

# Check if the guessed letter or word is in the secret word
def checking(guess, secret_word, reveal):
    #If player guess is the secret word then displays a congrats message
    if guess == secret_word:
        return secret_word, True

    word_reveal = ""
    #If guess is a letter of secret word then displays letters
    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            word_reveal += guess
        else:
            word_reveal += reveal[i]

    return word_reveal, False

# Display the game state, including the current hangman stage
def display_game(reveal, guessed_letters, choice, incorrect, fill_space):
    empty_space = " ".join(reveal)
    fill_space = " ".join(guessed_letters)
    print(f"Category: {choice}")
    print(f"Word: {empty_space}")
    print(f"Guessed letters: {fill_space}")
    print(display_hangman(incorrect))

# Hangman visual representation
def display_hangman(incorrect):
    stages = [
        """
         -----
             |
             |
             |
             |
             |
        =======
        """,
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
    fill_space = " "
    reveal = "_" * len(secret_word)

    while incorrect < max_incorrect:
        display_game(reveal, guessed_letters, choice, incorrect, fill_space)
        guess = player_guess(secret_word)
        #If player repeats an already guessed letter then this error message will be prompted
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters += guess

        reveal, correct_guess = checking(guess, secret_word, reveal)
        #Displays how many tries player has left
        if guess not in secret_word:
            incorrect += 1
            print(f"Woah oh! You have {max_incorrect - incorrect} tries left!")
        #Congratulations message
        if correct_guess or "_" not in reveal:
            print(f"Congrats! You got the hidden word {secret_word}!")
            break
    #When players runs out of guesses the secret word will show
    if incorrect == max_incorrect:
        print(f"Outta guesses! The hidden word was {secret_word}")
    #If player wiins or loses a play again question will be asked
    retry = input("Do you wish to play again? Yes or no: ").strip().upper()
    if retry == "YES":
        hangman()
    else:
        print("Thank you for playing!")

if __name__ == "__main__":
    hangman()
