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

for line in Lines:
	if numberofLines <= 0:
		break
	print(line)
	numberofLines -=1