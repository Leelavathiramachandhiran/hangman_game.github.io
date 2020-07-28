import time
import random
from words import word_list
def get_word():
    word=random.choice(word_list)
    return word
name=input("enter your name: ")
print("hello {} ,lets start our Hangman game!!!".format(name))

time.sleep(0.5)
print ("start your guesses..")
word=get_word()
guesses=""
turns=6
while turns>0:

    for char in word:
        failed=0
        if char in guesses:
            print(char)
        else:
            print("-")
            failed+=1
    if failed==0:
        print("you won")
        break


    guess=input("enter a character")
    guesses+=guess
    if guess not in word:
          turns-=1
          print("wrong")
          print("you left with {} turns now".format(turns))
          if turns==0:
              print("you lost the game!")
