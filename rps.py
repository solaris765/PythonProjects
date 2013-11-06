'''
A simple Rock Paper Scissors game
Algorithm:
1. Have the user input r, p, or s
2. Have the computer choose a random integer (1-3)
3. Tell the user the result of the game

Todo:
- Finish mode business
- Detect if a user is repeatedly throwing the same thing and counter that
- Sweet graphics(?)
'''
- Profit?

#Housekeeping
from random import randint
from random import seed
#from collections import Counter
seed()
a = 1
rock = 0
paper = 0
scissors = 0
playerlist = []

#Defining functions

def increment(x):
    #Function to incrememnt global vars based on user input
    if x == "r":
        global rock
        rock = rock+1
    elif x == "p":
        global paper
        paper = paper+1
    elif x == "s":
        global scissors
        scissors = scissors+1

def decon(x):
    #Functions to convert x to numbers for math
    if x == "r":
        x = 1
    elif x == "p":
        x = 2
    elif x == "s":
        x = 3
    return x

def convert(x):
    #Function to convert x to letters for printing
    if x == 1:
        x = "rock"
    elif x == 2:
        x = "paper"
    elif x == 3:
        x = "scissors"
    return x

def save_presult(x):
    #Function to append x to a list and save to txt
    out_file = open("player_rps_results.txt", "wt")
    out_file.write(', '.join(playerlist))
    out_file.write("\n")
    out_file.close()

def get_pmost_common(x):
    #Function to read the mode of x from the txt
    in_file = open("player_rps_results.txt", "rt")
    plist = in_file.read()
    in_file.close()
    pmc = plist.most_common()
    return plist.most_common()

#The important stuff
print("input q to quit")
print("r, p, s")
names = ['rock', 'paper', 'scissors']
while a == 1:
    x = str(input("Throw: "))
    if x!="r" and x!="p" and x!="s" and x!="q":
        continue
    elif x == "r" or x == "s" or x == "p":
        increment(x)
        cpu = randint(1, 3)
        player_result = ["ties with", "beats", "loses to"]
        result = player_result[(decon(x) - cpu) % 3]
        
        #Print result
        print(str(convert(decon((x)))).capitalize() + " " + str(result) + " " + str(convert(cpu)))
    
    elif x == "q":
        print("Goodbye")
        #Print player results to txt file
        save_presult(decon(x))
        break
