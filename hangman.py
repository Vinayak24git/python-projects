import random
from words import words
import string



def get_validword(words):
    word = random.choice(words) #randomly chooses something from the list
    while '-' in word or ' ' in word :
        word= random.choice(words)
        
    return word.upper()

def hangman():
    word = get_validword(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters=set() #what the user guessed
    
    lives=6
    
    #getting user input
    while len(word_letters) > 0 and lives > 0 :
        
        #letters used
        print("u have used this letter",' '.join(used_letters))
        
        #what the correct word is (W- R D)
        word_list= [letter if letter in used_letters else '-' for letter in word]
        print("current word: ", ' '.join(word_list))
        
        
        user_letters= input("guess a letter").upper()
        if user_letters in alphabet- used_letters:
            used_letters.add(user_letters)
            if used_letters in word_letters:
                word_letters.remove(user_letters)
            else:
                lives= lives-1 #take away a life if wrong
                print("letter is not in the word")
                
        elif user_letters in used_letters:
            print("u have already used the letter")
            
        else:
            print("invalid character") 
            
    #gets here when len(word_letters)== 0 or lives==0
    if lives==0:
        print("u died. the word is", word)
    else:
        print("u guessed the word correctly", word)
hangman()       