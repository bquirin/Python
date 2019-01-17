#Functions and Files
#import argv module from the sys package
from sys import argv

script, inputFile = argv

#define functions
def printAll(f):
    print(f.read())

def rewind(f):
    f.seek(0) # sets the pointer to the beginning of the file

def printALine(lineCount, f):
    print(lineCount, f.readline())

currentFile = open(inputFile)

printAll(currentFile)

print("Now let's rewind, kind of like a tape")

rewind(currentFile)

print("Let's print three lines:")

currentLine = 1
printALine(currentLine,currentFile)

currentLine += 1
printALine(currentLine,currentFile)

currentLine += 1
printALine(currentLine,currentFile)
