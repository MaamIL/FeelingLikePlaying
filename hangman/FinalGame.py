from colorama import Fore, Style
import random
import string
import hangman.ascii_art as ascii_art

def choose_word(file_path, index):
    """
    randomly choose a word from the words text file
    :param file_path: words text file
    :param index: random number for choosing word
    :return: word
    """
    with open(file_path, "r") as read_file:
        words = read_file.read().split(",")

    if index > len(words):
        index = index - len(words)
    return (words[index-1].replace('"',""))

def check_valid_input(letter_guessed, old_letters_guessed):
    """
    check if user's input of letter is valid. In case of ptoblem- will print a red X and describe issue.
    :param letter_guessed: letter inserted by user, to be checked
    :param old_letters_guessed: list of already guessed letters
    :return: True if ok, false if problem
    """
    abc = list(string.ascii_lowercase)
    letter_guessed = letter_guessed.lower()
    if len(letter_guessed) > 1:
        print(Fore.RED + 'X', Style.RESET_ALL + ' Only one letter please')
        return False
        
    elif letter_guessed not in abc:
        print(Fore.RED + 'X', Style.RESET_ALL + ' Not a letter')
        return False

    if letter_guessed in old_letters_guessed:
        print(Fore.RED + 'X', Style.RESET_ALL + ' Letter already guessed')
        print(old_letters_guessed)
        return False
    return True

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    update letter in the already guessed letters list
    :param letter_guessed: letter to be added
    :param old_letters_guessed: already guessed letters list
    :return: True
    """
    old_letters_guessed.append(letter_guessed.lower())
    return True

def show_hidden_word(secret_word, old_letters_guessed):
    """
    print word to screen, while letters not guessed yet will be printed as '_'
    :param secret_word: word to guess
    :param old_letters_guessed: already guessed letters list
    :return: word as the string that should be printed to screen
    """
    word_to_show = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            word_to_show += letter
        else:
            word_to_show += '_'
    return word_to_show

def print_hangman(num_of_tries_left):
    """
    print correct hangman status ascii art according to numbers of tries left (as indicated in HANGMAN_PHOTOS dictionary)
    :param num_of_tries_left: how many tries are left (also the index of the ascii art to be shown)
    """
    print("Hangman:\n\t",ascii_art.HANGMAN_PHOTOS[num_of_tries_left], "\n", "Tries left: ", num_of_tries_left)

def Get_letter(guessed_letters, word, num_of_tries_left):
    """
    get letter as user input. 
    check validation. 
    update list of guessed letters and number of tries accordingly.
    :param guessed_letters: list of guessed letters
    :param word: word to guess
    :param num_of_tries_left: number of tries left
    :return: updated number of tries left
    """
    letter_guessed = input("Guess a letter:  ")
    if check_valid_input(letter_guessed, guessed_letters):
        if letter_guessed not in word:
            num_of_tries_left -= 1
        try_update_letter_guessed(letter_guessed, guessed_letters)

    return num_of_tries_left

def check_win(secret_word, old_letters_guessed):
    """
    check if there is a win: a win will happen when all word letters are in the guessed list (=user guessed all letters)
    :param secret_word: word to guess
    :param old_letters_guessed: list of guessed letters
    :return: True in case of win, otherwise False
    """
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True

def Print_after_try(tries_left, secret_word, old_letters_guessed):
    """
    sequence to print after user's guess: 
    1. word to guess with '_' in non guessed letters 
    2. hangman status 
    3. number of tries left 
    4. list of used letters
    :param tries_left: number of tries left
    :param secret_word: word to guess
    :param old_letters_guessed: list of used letters
    """
    print("Word to guess (",len(secret_word),"):\n\t",show_hidden_word(secret_word, old_letters_guessed))
    print_hangman(tries_left)
    print("Letters used: ", old_letters_guessed)
    pass

def main():
    """
    initialize game (hangman title ascii art, num of tries- 6, the word's file),
    choose word and loop game tries till win or loose
    """
    print(ascii_art.HANGMAN_ASCII_ART)
    tries_left = 6
    letters_guessed = []
    file_words = "./hangman/words.txt"
    word_chosen = choose_word(file_words, random.randint(0,5000))
    while tries_left > 0 and not check_win(word_chosen, letters_guessed):
        Print_after_try(tries_left, word_chosen, letters_guessed)
        tries_left = Get_letter(letters_guessed, word_chosen, tries_left)
    if tries_left == 0:
        print_hangman(tries_left)
        print(Fore.RED + "\n\tYOU LOOSE!")
    elif check_win(word_chosen, letters_guessed):
        print_hangman(-1)
        print(Fore.LIGHTBLUE_EX + "YOU WIN!")

if __name__ == "__main__":
    main()