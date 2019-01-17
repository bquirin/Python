#imports sys module
from sys import argv

script, filename = argv

print("What is the name of the file you want to read?")
filename = input("> ")
txt = open(filename)

print("Here is your file {!r}".format(filename))
print(txt.read())
