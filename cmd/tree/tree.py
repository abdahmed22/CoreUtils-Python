import sys, os 

numberofDirectories = 1
numberofFiles = 0

def printDirectory(entry, level):
    print(f"|_{entry}")
    printDirectoryRecursion(entry, level, "    ")
    print(f"{numberofDirectories} directories, {numberofFiles} files")

def printDirectoryRecursion(entryName, level, space):

    if level == 0: 
        return

    c = os.listdir(entryName)

    if len(c) == 0:
        return 

    level -= 1

    for entry in c:
        fullPath = os.path.join(entryName, entry)
        if os.path.isdir(fullPath):
            numberofDirectories += 1
            print(f"{space}|_{entry}")
            printDirectoryRecursion(fullPath, level, space + "    ")
        else:
            numberofFiles += 1
            print(f"{space}|_{entry}")


treeLevel = 0
directoryName = ""

args = sys.argv[1:]

if len(args) > 3:
	print("Wrong Number of Arguments")
	sys.exit()

if args[0] == "-L" :
	treeLevel = int(args[1])
	directoryName = args[2]
elif len(args) == 0:
	treeLevel = -1
	directoryName = os.getcwd()
else :
    treeLevel = -1
    directoryName = args[0]
    
printDirectory(directoryName, treeLevel)
     

