import sys

temp = 10
args = sys.argv[1:]

if len(args) == 0:
    while temp > 0:
        print("y")
else:
    while temp > 0:
        for word in args:
            print(word, end=" ")
        print()
