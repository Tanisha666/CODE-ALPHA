import random

def choose_word():
    # List of words to choose from
    words = ["python", "hangman", "programming", "computer", "algorithm", "developer", "coding"]
    return random.choice(words)

def display_word(word, guessed_letters):  
    # Display the word with guessed letters and underscores for unguessed letters
    display = [letter if letter in guessed_letters else '_' for letter in word]     
    return ' '.join(display)   

def hangman():
    # Select a random word  
    word = choose_word()   
    guessed_letters = set()                         
    max_incorrect_guesses = 6  # Maximum allowed incorrect guesses      

    print("Welcome to Hangman!")    
    print(f"The word has {len(word)} letters.")     
   
    while incorrect_guesses < max_incorrect_guesses:
        print(display_word(word, guessed_letters))
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")             
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():     
            print("Please enter a single letter.\n")       
            continue          

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try another letter.\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.\n")
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.\n")

        # Check if all letters have been guessed
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You've guessed the word: {word}")
            break
    else:
        print(f"Game over! You've run out of guesses. The word was: {word}")

# Run the game
hangman()
