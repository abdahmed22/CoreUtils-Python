import sys

numberofLines = 0


fileName = ""

args = sys.argv[1:]

if len(args) == 0 or len(args) > 3:
	print("Wrong Number of Arguments")
	sys.exit()

if args[0] == "-n" :
	numberofLines = int(args[1])
	fileName = args[2]
else :
	numberofLines = 10
	fileName = args[0]

file = open(fileName, 'r')
Lines = file.readlines()
file.close()

if len(Lines) < numberofLines:
	numberofLines = len(Lines)

start = len(Lines) - numberofLines
finish = len(Lines)

for i in range(numberofLines):
	if start == finish:
		break
	print(Lines[start])
	start +=1