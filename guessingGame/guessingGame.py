import random
import os
import shutil
import time as t
from lagerMappe import makeFile

def clear():
    if os.name == "nt":
        os.system('cls')
clear()

# Array of messages
array = [
    "Det er",                           # 0
    "Drumroll ??",                      # 1 
    "🥁",                               # 2 
    "Riktig🥳",                         # 3
    "Feil😡",                           # 4
    "Det riktige nummeret var",         # 5
    "!!!",                              # 6 
    "Si hade til filene dine 😎 !!!",   # 7
    "er borte vekk",                    # 8
    "heheheha😁",                       # 9
    "Hmmmmmmmmmmmmmm🤔🤔🤔🤔🤔🤔🤔", # 10
    "☝️",                               # 11
    "jeg har en mester plan🤓🤓"       # 12
]

# Generate a random number between 1 and 10
randomNumber = random.randint(1, 10)
print(f"(DEBUG) Random number: {randomNumber}")  # For debugging; you can remove this line
userGuessNumber = int(input("Gjett nummer 1 - 10?   "))

# Directory and file details
directory = r"mappeMedVeldigViktigeFiler;)"

if userGuessNumber == randomNumber:
    print(array[0])
    t.sleep(1)
    print(array[1])
    t.sleep(1)
    for i in range(4):
        print(array[2])
        t.sleep(0.2)          
    print(array[3])
    t.sleep(1)
    print(array[10])
    t.sleep(3)
    print(array[11])
    t.sleep(0.7)
    print(array[12])
    t.sleep(2.5)
    clear()
    makeFile()
    t.sleep(3)
    print(array[7])
    t.sleep(1.5)
    if os.path.exists(directory):
        shutil.rmtree(directory)
        print(f"{directory} {array[8]}")
        t.sleep(3)
        print(array[9])
else:
    t.sleep(1)
    print(array[0])
    t.sleep(1)
    print(array[1])
    t.sleep(1)
    for i in range(4):
        print(array[2])
        t.sleep(0.2)          
    print(array[4])
    t.sleep(1)
    print(f"{array[5]} {randomNumber} {array[6]}")
    t.sleep(2)
    print(array[7])
    t.sleep(1.5)
    if os.path.exists(directory):
        shutil.rmtree(directory)
        print(f"{directory} {array[8]}")
        t.sleep(3)
        print(array[9])
        t.sleep(5)
    else:
        print("FILENE FINNES IKKE ?? 😱😱😱")
        t.sleep(5)
clear()