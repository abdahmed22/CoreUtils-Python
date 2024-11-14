import sys

numberofLines = 0
numberofWords = 0
numberofCharacters = 0

fileName = ""

numberofLinesFlag = False
numberofWordsFlag = False
numberofCharactersFlag = False


args = sys.argv[1:]

if len(args) == 0:
    print("Wrong Number of Arguments")
    sys.exit()

if "-l" in args:
    numberofLinesFlag = True

if "-w" in args:
    numberofWordsFlag = True

if "-c" in args:
    numberofCharactersFlag = True

if not (numberofLinesFlag) and not (numberofWordsFlag) and not (numberofCharactersFlag):
    numberofLinesFlag = True
    numberofWordsFlag = True
    numberofCharactersFlag = True

fileName = args[-1]

if fileName[0] == "-":
    print("Wrong Number of Arguments")
    sys.exit()

file = open(fileName, "r")
Lines = file.readlines()
file.close()

if numberofLinesFlag:
    for line in Lines:
        numberofLines += 1
    print("Number of Lines :", numberofLines)

if numberofWordsFlag:
    for line in Lines:
        words = line.split(" ")
        numberofWords += len(words)
    print("Number of Words :", numberofWords)

if numberofCharactersFlag:
    for line in Lines:
        words = line.split(" ")
        for word in words:
            numberofCharacters += len(word)
    print("Number of Characters :", numberofCharacters)
