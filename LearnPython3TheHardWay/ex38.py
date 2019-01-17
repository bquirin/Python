#Doint things to lists

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there's not 10 things in that list, let's fix that")

stuff = ten_things.split(" ") #in: string, defined seperator |out: list
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print("There's {:d} items now".format(len(stuff)))

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) #whoa fancy
print(stuff.pop())
print(' '.join(stuff)) # in: list out: sting with elements from list
print("#".join(stuff[3:6])) #slice stuff list and then join each element with #



# dir() shows you all the methods and attr associated with the instance
