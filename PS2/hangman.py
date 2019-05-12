
import random
import string
import os

os.chdir('ps2')

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for char in secret_word:
      if char not in letters_guessed:
        return False
    return True



def get_guessed_word(secret_word, letters_guessed):
    wordprinted = ''
    for char in secret_word:
      if char not in letters_guessed:
        wordprinted += "_"
      else:
        wordprinted += char
    return wordprinted
        


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters = ''
    for char in string.ascii_lowercase:
      if char not in letters_guessed:
        available_letters += char
    return available_letters


    

def hangman(secret_word):
    print ('welcome to hangman')
    print('I am thinking of a word ' + str(len(secret_word)) + ' letters long')
    guesses_left = 6
    warnings_left = 3
    letters_guessed = []
    print(get_guessed_word(secret_word, letters_guessed))
    print('You have {} warnings left'.format(warnings_left))
    

    while guesses_left > 0 and not is_word_guessed(secret_word,letters_guessed):
      print('You have {} guesses left'.format(guesses_left))
      z = str(get_available_letters(letters_guessed))
      print('Available letters: ' + z)

      guess = input('Letter:').lower()
      
      if not str.isalpha(guess):
        if warnings_left > 0:
          warnings_left -= 1
        else:
          guesses_left -= 1
      
      else:
        guess = str.lower(guess)

        if guess in letters_guessed:
          if warnings_left > 0:
            warnings_left -= 1
          else:
            guesses_left -= 1

        else:
          letters_guessed.append(guess)
          if guess in secret_word:
            print ("Good guess")
            print(get_guessed_word(secret_word, letters_guessed))
          else:
            if guess in ('a','e','i','o','u'):
              guesses_left -= 2
            else:
              guesses_left -= 1
            print("wrong")
            print(get_guessed_word(secret_word, letters_guessed))

    if is_word_guessed(secret_word,letters_guessed):
      print("You won")
    else:
      print("Sorry, you lost")




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)