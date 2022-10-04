from pickle import TRUE
import random

# -------------------------------------------------------------------------------------------------------------------------
 # A function that reads a text file of words and randomly selects one to use as the secret wordfrom the list.

def load_word():
   
   
    '''Returns: 
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
    for i in secret_word:
        if i not in letters_guessed:
            return False
            else: return True
    # if letters_guessed in secret_word == True:
    
    # # letters_guessed (list of strings): list of letters that have been guessed so far.
    #   Args:
    #     secret_word (string): the random word the user is trying to guess.
    
    
 
        # bool: True only if all the letters of secret_word are in letters_guessed, False otherwise


    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
def guessed( guess, secret_word):
    letters_guessed.append(guess)

           
            #    pass

# -----------------------------------------------------------------------------------------------------
#  A function that is used to get a  
# 

def get_guessed_word(secret_word, letters_guessed, word_to_guess):
    i = 0
    while i < len(secret_word):
        if secret_word[i] in letters_guessed:
            word_to_guess[i] = secret_word[i]
        i += 1

    '''
   
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet

   

# ----------------------------------------------------------------------------------------------------------

def is_guess_in_word(guess, secret_word):
    if guess in secret_word:
        correct_guess.append(guess)
        return True
    else: 
        incorrect_guess.append(guess)
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

    pass


# -----------------------------------------------------------------------------------------------------------
# Show the player information about the game according to the project spec

print("Welcome to Spaceman-The Guessing Game!" "\n \n" 
"You are allowed 7 incorrect guesses." "\n"
"If you can guess the word before running out guesses you win!" "\n")

player_ready = input("You ready? y or n? ")

if player_ready == "y".lower(): ("\n")
print("Let's a go!!!")


#  -----------------------------------------------------------------------------------------------------------

# TODO Ask the player to guess one letter per round and check that it is only one letter

guessed_letter = 0
user_input = input("Guess one letter: ")
if guessed_letter < 0:
    print("Please only choose one letter!")


    
# -----------------------------------------------------------------------------------------------------------
# A function that controls the game of spaceman. Will start spaceman in the command line.
    # Args:
    #   secret_word (string): the secret word to guess.
    

# def spaceman(secret_word):
   

    

    #TODO: Ask the player to guess one letter per round and check that it is only one letter


    #TODO: Check if the guessed letter is in the secret or not and give the player feedback

    #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost






#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)


# import random

# # ------------------------------------------------------------------------------
# # reads a text file of words and randomly selects one to use as the secret word from the list

# def load_word():

#     f = open('words.txt', 'r')
#     words_list = f.readlines()
#     f.close()
    
#     words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
#     secret_word = random.choice(words_list)
#     return secret_word




# # ------------------------------------------------------------------------------
# # DEFINE IF ALL LETTERS OF SECRET WORD HAVE BEEN GUESSED

# def is_word_guessed(secret_word, letters_guessed):
#   for letter in secret_word: 
#     if letter not in letters_guessed:
#         return False


#     '''
#     A function that checks if all the letters of the secret word have been guessed.

#     Args:
#         secret_word (string): the random word the user is trying to guess.
#         letters_guessed (list of strings): list of letters that have been guessed so far.
    
#     Returns: 
#         bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
#     '''

#     # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
   
    
# def get_guessed_word(secret_word, letters_guessed):
#     random_word = ""
#     for letter in secret_word:
#         if letter in letters_guessed:
#             random_word += letter + ""
#         else:
#                 random_word += "_"
#     return random_word



#     '''
#     A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

#     Args: 
#         secret_word (string): the random word the user is trying to guess.
#         letters_guessed (list of strings): list of letters that have been guessed so far.

#     Returns: 
#         string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
#     '''

#     #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet

# #-----------------------------------------------------------------  

# '''
#     A function to check if the guessed letter is in the secret word

#     Args:
#         guess (string): The letter the player guessed this round
#         secret_word (string): The secret word

#     Returns:
#         bool: True if the guess is in the secret_word, False otherwise

#     '''

#     #TODO: check if the letter guess is in the secret word

# def is_guess_in_word(guess, secret_word):
#         if guess in secret_word:
#             print("You guessed a correct letter!")
#             return True

#         else:
#             print("Sorry, that letter isn't in the word, try again!")
#             return False



# # -------------------------------------------------------------
# #These function calls that will start the game

# '''
#     A function that controls the game of spaceman. Will start spaceman in the command line.


#     Args:
#       secret_word (string): the secret word to guess.
# '''
# def spaceman(secret_word):{

# }



# letters_guessed = " "
# incorrect_guesses = 0
# correct_guesses = 0
# chances = 7


# # -------------------------------------------------------------
# #
# while chances > 0:
#     print("You have {chances} remaining!")

#     output += letter
#     for letter in word:
#         if letter in correct_guesses:
#             letters_guessed += letter
#             else: output += '_'

#         if output == word:
#             break
#         print("Guess the word: ")
#         print(chances," chances left")
#         guess = input().lower(

#         if guess in correct_guesses or guess in incorrect_guesses:
#                 print("Already guessed", guess)
#                 elif guess in word:
#                     print("Noice! That letter is in the word!")
#                     else: print("Bummer! That letter isn't in the word!")
#                     spaceman_count = spaceman_count + 1
#                     chances = chances -1
#                     incorrect_guess.append(guess)
#                     print(spaceman_count)

#         if chances > 0:
#             print(" Winner winner, chicken dinner! You got it!")
#             else:
#                 print("Dang, you guessed wrong. Try again.")


#         )






# '''
# # --------------------------------------------------------------

#     #TODO: Check if the guessed letter is in the secret or not and give the player feedback

#     #TODO: show the guessed word so far

# 
#    #TODO: check if the game has been won or lost
# '''






