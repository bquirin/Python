#More Variables and Printing

myName = "Brandon Q"
myAge  = 35 # not a lie
myHeight = 74 # inches
myWeight = 180 #lbs
myEyes = "Blue"
myTeeth = "White"
myHair = "Brown"

print(f"Let's talk about {myName}")
print(f"He's {myHeight} inches tall")
print(f"He's {myWeight * 0.453592} pounds heavy")
print("Actually that is not too heavy")
print(f"He's got {myEyes} eyes and {myHair} hair")
print(f"His teeth are usually {myTeeth} depending on the coffee")

#This line is tricky, try to get it exactly right
total = myAge + myHeight + myWeight
print(f"If I add {myAge}, {myHeight}, and {myWeight} I get {total}")
