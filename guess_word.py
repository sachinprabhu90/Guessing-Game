import json
import  subprocess
import random
from collections import Counter

def game(cleaned_words):
    len_words = len(cleaned_words)
    subprocess.call('figlet Guess My Word!!',shell=True) # only works if figlet is installed
    print('There are {} words with unrepeated chars this machine will randomly choose from!'.format(len_words))
    random_word = cleaned_words[random.randint(0,len_words)]
    print('The  word chosen is {} chars long and you get {} chances'.format(len(random_word),len(random_word)+3))
    chance = len(random_word)+3
    #print(random_word) #for testing
    guessed_words = []
    for i in range(0,len(random_word)):
        guessed_words.append('*') # populating garbage
    while chance >=0:
        if ''.join(guessed_words) == random_word:
            print('Good Game! You guessed {} right!'.format(random_word))
            break
        if ''.join(guessed_words)!=random_word and chance==0:
            print('You have exhausted your guesses! The word was {}'.format(random_word))
            print('Better luck next time')
            break
        guessed_char = input('Enter the guessed_char: ')
        if isinstance(guessed_char,str) and len(guessed_char)==1:
            if guessed_char in random_word:
                # if a character is repeated, this  will select the first one
                # code needs to handle this
                found_index = random_word.index(guessed_char)
                print('Awesome! {} is found at the place {}, you have {} guesses left'.format(guessed_char,found_index,chance))
                if guessed_words[found_index] == '*':
                    guessed_words[found_index] = guessed_char
                chance-=1
                print(guessed_words)
            else:
                chance-=1
                print('{} is not in the random word, you have {} guesses left'.format(guessed_char,chance))
        else:
            print('Please enter 1 character at a time, you have {} guesses left'.format(chance))




with open('unrep_words_True.json','r') as file:
    cleaned_words = json.load(file)

game(cleaned_words)
