import random
import time

# Invitation in the game

print("\nWelcome to HANGMAN game by Arvind S.\n")

name = input("Enter your name: ")
print(f"Hello {name}.! All the Best!")
time.sleep(3)
print("Wait, The game is about to start...\n")
time.sleep(4)
print("Lets play the game!!!")


def main():

    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ['republic','purple','cauliflower','february','september','technology','python','independence','scientist','multiply','descending']
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_'*length
    already_guessed = []
    play_game = ""


def play_loop():
    global play_game
    play_game = input("Do you want to play again? y= Yes, n= No: ")
    while play_game not in ['y','n']:
        play_game = input("Do you want to play again? y = Yes , n = No: ")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thank you!!\nHope to see you again.")
        
    
def hangman():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    limit = 5
    guess = input(f"Enter your guess(No: of letters are {length}): ")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= '9':
        print("Invalid Input, Try a letter instead\n")
        hangman()
    elif guess in word:
        already_guessed.append(guess)
        index = word.index(guess)
        word = word[:index] + '_' + word[index+1:]
        display = display[:index] + guess + display[index+1:]
        print(display + '\n')
    elif guess in already_guessed:
        print('Already entered,Try another letter\n')
    else:
        count += 1
        if count == 1:
            time.sleep(1)
            print("     _____\n"
                  "    |     \n"
                  "    |     \n"
                  "    |     \n"
                  "    |     \n"
                  "    |     \n"
                  "    |     \n"
                  "    |     \n"
                  "  __|__   \n")
            print("wrong guess! " + str(limit - count) + " guesses remainging")
        elif count == 2:
            time.sleep(1)
            print("     _____  \n"
                  "    |     | \n"
                  "    |       \n"
                  "    |       \n"
                  "    |       \n"
                  "    |       \n"
                  "    |       \n"
                  "    |       \n"
                  "  __|__     \n")
            print("wrong guess! " + str(limit - count) + " guesses remainging")

        elif count == 3:
            time.sleep(1)
            print("     _____   \n"
                  "    |     |  \n"
                  "    |     |  \n"
                  "    |        \n"
                  "    |        \n"
                  "    |        \n"
                  "    |        \n"
                  "    |        \n"
                  "  __|__      \n")
            print("wrong guess! " + str(limit - count) + " guesses remainging")

        elif count == 4:
            time.sleep(1)
            print("     _____   \n"
                  "    |     |  \n"
                  "    |     |  \n"
                  "    |     |  \n"
                  "    |        \n"
                  "    |        \n"
                  "    |        \n"
                  "    |        \n"
                  "  __|__      \n")
            print("wrong guess! " + str(limit - count) + " guesses remainging")
            
        elif count == 5:
            time.sleep(1)
            print("     _____    \n"
                  "    |     |   \n"
                  "    |     |   \n"
                  "    |     |   \n"
                  "    |     O   \n"
                  "    |    /|\  \n"
                  "    |    / \  \n"
                  "    |         \n"
                  "  __|__       \n")
                    
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:",already_guessed,word)
            play_loop()
        
    if word == '_' * length:
        print("Congrats!, You have guessed the word correctly!")
        play_loop()
        
    elif count != limit:
        hangman()

main()
hangman()

            





