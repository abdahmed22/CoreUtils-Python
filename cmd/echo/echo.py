import sys

newLine = False

args = sys.argv[1:]

if len(args) == 0:
    print("Wrong Number of Arguments")
    sys.exit()

if args[0] == "-n":
    newLine = True
    args = args[1:]

if len(args) != 0:
    for word in args:
        if newLine:
            print(word)
        else:
            print(word, end=" ")
if not (newLine):
    print()
