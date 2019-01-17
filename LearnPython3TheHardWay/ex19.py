#Functions and Variables

def cheeseAndCrackers(cheeseCount, boxOfCrackers):
    print(f"You have {cheeseCount} cheeses!")
    print(f"You have {boxOfCrackers} boxes of crackers")
    print("Man that's enough for a party!")
    print("Get a blanket. \n")

print("We can just give the function numbers directly:")
cheeseAndCrackers(20,340)

print("OR, we can use variables from our script:")
amountOfCheese = 10
amountOfCrackers = 50

cheeseAndCrackers(amountOfCheese,amountOfCrackers)

print("We can even do math inside too:")
cheeseAndCrackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheeseAndCrackers(amountOfCheese + 100, amountOfCrackers + 1000)

def Sum(num1,num2):
    sum = num1 + num2
    print(sum)

Sum(10,100)
