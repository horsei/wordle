

import random
import sys
# to clear the terminal and make the game user friendly
import termcolor
from colorama import Fore, Back, Style, init
from termcolor import colored
init(convert=True)


def print_menu():
    print("welcome to wordle !")
    print("type a 5 letter word and hit enter\n")


def read_random_word():
    with open('E:\kartikey\crores_pa\programs\python\wordle\words.txt') as word_database:

        # splitline so every line in the text file gets stored as a diferent array
        # block and since here every line is basically a word so every word gets stored as an individual array.

        words = word_database.read().splitlines()
        return random.choice(words).lower()

def word_repeat_check():
    wordrepeat=[];
    for i in range(5):
        count=0;
        for j in range(5):
            if(word[i]==word[j]):
                count=count+1;
                
        if (count>0):
            wordrepeat.append(count);
            
    print(wordrepeat);

def guess_repeat_check():
    guessrepeat=[];
    for i in range(5):
        count=0;
        for j in range(5):
            if(guess[i]==guess[j]):
                count=count+1;
                
        if (count>0):
            guessrepeat.append(count);
            
    


print_menu()
play_again = ""

while play_again != "quit":

    word = read_random_word()
    wordrepeat=[];
    for i in range(5):
        count=0;
        for j in range(5):
            if(word[i]==word[j]):
                count=count+1;
                
        if (count>0):
            wordrepeat.append(count);
            
     
    
    with open('E:\kartikey\crores_pa\programs\python\wordle\words.txt') as f:
        if word in f.read():

            for attempt in range(1, 7):

                guess = input().lower()
                
                guessrepeat=[];
                for i in range(5):
                    count=0;
                    for j in range(5):
                        if(guess[i]==guess[j]):
                            count=count+1;
                            
                    if (count>0):
                        guessrepeat.append(count);

                sys.stdout.write('\x1b[1A')
                sys.stdout.write('\x1b[2K')
            
                

                for i in range(min(len(guess), 5)):
                    if guess[i] == word[i]:

                        # end="" is used so it doesnt go to a new line after printing the coloured letter

                        print(colored(guess[i], 'green'), end="")
                    elif guess[i] in word:
                        
                    
                        print(colored(guess[i], 'yellow'), end="")

                    else:
                        print(guess[i], end="")

                print()

                if guess == word:
                    print((f"\nyou got the word in {attempt} tries !"))
                    break
                elif attempt == 6:

                    print(f"sorry the wordle was " +
                          colored(word, 'cyan') + ":(")
        else:
            print("invalid word")

    play_again = input("\ntype quit to exit otherwise click enter")

