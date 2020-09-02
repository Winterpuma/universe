import os
import sys

os.system('color')

RED = '\033[91m'
YELLOW = '\033[93m'
ENDC = '\033[0m'

if (len(sys.argv) != 3):
    print("You must specify a path to file and word via args")
else:
    word = sys.argv[2].lower()
    wordcount = 0
    curpos = 0
    wordlen = len(word)
    with open(sys.argv[1], 'r', encoding="utf-8") as file:
        data = file.read()
    for ch in data:
        if (ch.lower() == word[curpos]):
            curpos = (curpos + 1) % wordlen
            if curpos == 0:
                wordcount += 1
            print(RED + ch + ENDC, end='')
        else:
            print(ch, end='')
    print(YELLOW + '\n\nTotal amount of "' + word + '" = ' + str(wordcount) + ENDC)
