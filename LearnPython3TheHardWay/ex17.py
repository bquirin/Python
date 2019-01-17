from sys import argv
from os.path import exists

script, fromFile, toFile = argv

open(toFile,'w').write(open(fromFile).read())
print("Copied from {} to {}".format(fromFile,toFile))
