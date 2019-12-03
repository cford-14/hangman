#Hangman
import random


#def hangman fuction
def hangman(spelling_word_list):
    #if there are words on the spelling list, "welcome, do you want to play?"
    if spelling_word_list:

        print("Welcome to hangman!\n")
        #get input
        play = input("Do you want to play? \nEnter y for yes or n for no.\n")

        if play == "n":
            print("maybe later...")

        elif play == "y":
            #call the play the game function which chooses a word and sets up the game
            play_the_game(spelling_word_list)

        else:
            #checks for answers other than y and n and restarts hangman function
            print("Invalid entry")
            hangman(spelling_word_list)

    else:
        #tells the user that the list is empty
        print("The spelling list is empty! All of the words have been guessed!")


#define play the game fuction                    
def play_the_game(spelling_word_list):
    
    #pick the word randomly using random index
    list_index = random.randint(0, len(spelling_word_list)-1)

    #sets the spelling word as the viariable "word
    word = spelling_word_list[list_index]

    #find the length of the word, tell length/show lenght
    word_lenght = len(word)

    print("There are {0} letters in this word.".format(word_lenght))

    #establishing the word as a list items and the hangman lines as guess_word list
    word_list = []
    for i in word:
        word_list.append(i)

    guess_word = []
    for i in word:
        guess_word.append("_")

    #starts the game py printing the spaces
    print(guess_word)

    #calls the guessing fuction which allows the user to enter guesses
    guessing(word_list, guess_word, word)

    #removes the guessed word from the spelling list
    spelling_word_list.pop(list_index)

    #asks if user would like to play again and collects input of y or n
    play_again = input("Thanks for playing! \n\nWould you like to play again? \nEnter y for yes or n for no.\n")

    if play_again == "n":
        print("maybe later...")

    #recursive run of play the game function if the user wants to play again
    elif play_again == "y":
        play_the_game(spelling_word_list)

    #resarts the hangman fuction if the user has an invalid entry
    else:
        print("Invalid entry")
        hangman(spelling_word_list)



#define internal guessing fuction
def guessing(word_list, guess_word, word):          
    count = 0
    #gives 10 tries to guess the word
    while count < 10:
        if "_" not in guess_word:
            print("You Win! The word was \'{0}\'.".format(word))
            break
        #enter letter
        letter_guess = input("Please enter a lower case letter.\n")

        #checks for alphabet letter
        if not letter_guess.isalpha():
            print("Invalid entry.\n")

        else:
            # inecrements counter if wrong answer
            if letter_guess not in word_list:
                count +=1
                print("Uh oh! {0} is not in my word. You have {1} more wrong gueses.".format(letter_guess, 10-count))
                print(guess_word)
                if count >= 10:
                    print("You lose. The word was \'{0}\'".format(word))
                    break

            #replaces letter in the word and prints new hangman lines with correct letters entered
            else:
                for i in range(len(word_list)):
                    if word_list[i] == letter_guess:
                        guess_word[i] = letter_guess
                        word_list[i] = "_"
                print(guess_word)
                
                

spelling_Oct_21 = ["main", "weight", "say", "away", "play", "raise", "brain", "paint", "stay", "today", "tray", "tail", "everybody", "sorry"]    
    
    #loop: check if letter in word, up count or show letter in blank word 

hangman(spelling_Oct_21)
