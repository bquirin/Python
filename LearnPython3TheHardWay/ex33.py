
def printNumbers(stop, increment):

    i = 0 #initialize i
    numbers = [] #declare empty list

    while i < stop:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += increment
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


#print("The numbers: ")

#for num in numbers:
#    print(num)

#printNumbers(100,5)


def printNumbers2(stop, increment):
    numbers = []
    for num in range(0, stop, increment):
        numbers.append(num)
        num += increment
        print("Numbers now: ", numbers)



printNumbers2(100,5)
