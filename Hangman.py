import getpass
import os
import random
import time
import colorama
from colorama import Fore, Back, Style


HANGMANPICS= ["""

    +---+
    |   |
        |
        |
        |
        |
  =========""",'''
 
    +---+
    |   |
    O   |
        |
        |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========''']


def Password(text):
    length=len(text)
    temp=0
    text1=""
    tmstr="\0"
    key1=17
    for i in range(0,length):
        ord1=ord(text[i])
        if ord1>=97 and ord1<=122:
            temp=ord1+key1
            if temp>122:
               ord2=temp-122
               ordf=96+ord2
            else:
                ordf=ord1+key1
            
        elif ord1>=65 and ord1<=90:
            temp=ord1+key1
            if temp>90:
                ord2=temp-90
                ordf=64+ord2
            else:
                ordf=ord1+key1
        else:
            ordf=ord1
        text1=text1+chr(ordf)
    return text1


def GetAllEnglishWords():
    wordslist = []
    for line in open('hangman_english_words.txt'):
        line=line.rstrip()
        wordslist.append(line)
    return wordslist


def GetRandomWord(words):
    ran = random.randrange(0,len(words))
    return words[ran]


def Play(answer):
    word = answer
    mis = 0
    allow = 6
    newans = list('_'*len(word))
    already_guessed = []
    print('You have ',6-mis,' Lives.\n')
    print(' '.join(newans))
    while(mis < allow):
        if '_' not in newans:
            print('You Won')
            return True
        
        print(Fore.YELLOW+HANGMANPICS[mis]+ Style.RESET_ALL)
        print("\n")
        guess = input(Fore.WHITE+Back.YELLOW +'Guess:'+ Style.RESET_ALL)
        time.sleep(0.02)
        os.system('cls')
        
        if len(guess) > 1 or guess.isalpha() == False:
            print(Fore.RED +"Illegal Input: Try Again \n"+ Style.RESET_ALL)
            print(' '.join(newans))
            continue
        guess = guess.lower()
        if guess in already_guessed:
            print('You have already guessed',guess,'. Try again. \n')
            print(' '.join(newans))
        else:
            already_guessed.append(guess)
            if guess in word:
                print('Good guess! Continue. \n')
                for pos in range(0,len(word)):
                    if (word[pos] == guess):
                        newans[pos] = guess
                print(' '.join(newans))
            else:
                mis+=1
                if 6-mis==0:
                    print(guess,' is not in the word. You have Lost \n')
                else:
                    print(guess,' is not in the word. You have ',6-mis,' Lives \n')
                print(' '.join(newans))
    print(Fore.YELLOW+HANGMANPICS[mis]+ Style.RESET_ALL)
    print("\n")
    print("The correct word is ",word)
    print("\n")
    return False

            
def Username(name):
    with open("users.txt") as file:
        a=list(file.read().split(','))
    
        

def StartupAndPlay():
    Play(GetRandomWord(GetAllEnglishWords()))
    yesorno = input('Do you want to play again?(Y/N)')
    if yesorno.upper() == 'Y':
        return StartupAndPlay()
'''if __name__ == "__main__":
    StartupAndPlay()'''




def GetPlayRecord():
    with open("hangman_play_record.txt") as file:
        d = list(file.read().split(","))
        d[0] = int(d[0])
        d[1] = int(d[1])
    return d
ans = GetPlayRecord()    
    


def RecordPlay(win):
    with open ("hangman_play_record.txt") as a_file:
        a = list(a_file.read().split(","))
        if win:
            a[0] = int(a[0]) + 1
        a[1] = int(a[1]) + 1
        a[0] = str(a[0])
        a[1] = str(a[1])
        
    
    with open ("hangman_play_record.txt","w") as a_file:
        a_file.write(",".join(a))
    


def StartupAndPlayVersion2():
    record = GetPlayRecord()
    print("Total number of wins:",record[0])
    print("Total games played: ",record[1])
    print("\n")
    time.sleep(2)
    os.system('cls')
    ans=Play(GetRandomWord(GetAllEnglishWords()))
    RecordPlay(ans)
    a_record=GetPlayRecord()
    print("Total number of wins:",a_record[0])
    print("Total games played: ",a_record[1])
    yesorno=Play_again()
    if yesorno:
        os.system('cls')
        return StartupAndPlayVersion2()
    

def Play_again():
    yesorno=input('\nDo you want to play again?(Y/N)')
    if yesorno.upper() == 'Y':
        return True
    elif yesorno.upper()=='N':
        return False
    else:
        return Play_again()
            
def playstart():
    if __name__ == "__main__":
        StartupAndPlayVersion2()

passw=getpass.getpass("Please enter your password:")

if Password(passw)=="jldzk":
    time.sleep(.5)
    os.system('cls')
    playstart()
else:
    print("WRONG PASSWORD:::: ENDING")
os.system("pause")
