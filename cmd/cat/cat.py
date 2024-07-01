import sys

numberLines = False

args = sys.argv[1:]

if len(args) == 0:
    print("Wrong Number of Arguments")
    sys.exit()

if args[0] == "-n":
    numberLines = True
    args = args[1:]
i = 1
for fileName in args:
    file = open(fileName, "r")
    Lines = file.readlines()
    file.close()

    for line in Lines:
        if numberLines:
            print(i, " ", line)
            i += 1
        else:
            print(line)
