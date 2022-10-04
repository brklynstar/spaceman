import random

# -------------------------------------------------------------------------------------------------------------------------
 # A function that reads a text file of words and randomly selects one to use as the secret wordfrom the list.

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

# -------------------------------------------------------------------------------------------------------------------------
# A function that checks if all the letters of the secret word have been guessed.

def is_word_guessed(secret_word, letters_guessed):
    counter = 0
    correct_letters = 0
    for letter in secret_word:
        if letter in letters_guessed:
            correct_letters += 1
            return False
        else:
            counter += 1
            return True
    
    # # letters_guessed (list of strings): list of letters that have been guessed so far.
    #   Args:
    #     secret_word (string): the random word the user is trying to guess.
    
    
 
        # bool: True only if all the letters of secret_word are in letters_guessed, False otherwise


    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed

           
    

# -----------------------------------------------------------------------------------------------------
#  A function that is used to get guessed word
# 

def get_guessed_word(secret_word, letters_guessed):
    for letter in secret_word:
        if letter in letters_guessed:
            correctly_guessed += letter
        else: correctly_guessed += " _ "
    return correctly_guessed

    ''' 
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet

   

# ----------------------------------------------------------------------------------------------------------
# A function that is used to get guessed word

def is_guess_in_word(guess, secret_word):
    if guess in secret_word:
        return True
    else:
        return False
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word


# -----------------------------------------------------------------------------------------------------------
# Show the player information about the game according to the project spec
def spaceman(secret_word):
   
    print("Welcome to Spaceman-The Guessing Game!" "\n \n" 
    "You are allowed 7 incorrect guesses." "\n"
    "If you can guess the word before running out guesses you win!" "\n")

letters_guessed = []
lives = 7
secret_word = load_word()
spaceman(secret_word)

play = True
while play:
    guess = input("Guess only one letter: ") # TODO Ask the player to guess one letter per round and check that it is only one letter
    print("***************************")
    if is_guess_in_word(guess, secret_word):
        print("You got a letter correct!")
        letters_guessed.append(guess)
        print(f" Used letters: {letters_guessed}")
    else:
        lives -= 1
        print(f"{guess} is incorrect. But you still have {lives} guesses left.")
        letters_guessed.append(guess)
        print(f"Letters you've used: {letters_guessed}")

    if is_word_guessed(secret_word, letters_guessed):
        if lives == 0:
            print(f"Sorry, no more guesses, the word was {secret_word}")
            play = False
            break
    
  
# -----------------------------------------------------------------------------------------------------------
# A function that controls the game of spaceman. Will start spaceman in the command line.
    # Args:
    #   secret_word (string): the secret word to guess.
    


   

    

    #TODO: Ask the player to guess one letter per round and check that it is only one letter


    #TODO: Check if the guessed letter is in the secret or not and give the player feedback

    #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost






#These function calls that will start the game


