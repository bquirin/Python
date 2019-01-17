from sys import exit

def start():
    print("You are in the dark and there are two rooms available.")
    print("Do you pick room '1' or room '2'")

    answer = input("> ")

    if answer == "1":
        monsterRoom()
    elif answer == "2":
        moneyRoom()
    else:
        dead()

def monsterRoom():
    print("The monsters sleeping")
    print("Do you sneak round hum or run around him?")

    answer = input("> ")

    if answer == "sneak":
        dead()
    elif answer =="run":
        moneyRoom()
    else:
        print("The monster woke up and killed you")
        dead()

def moneyRoom():
    print("Your in the money room how much money do you take?")
    answer = int(input("> "))

    if answer > 100:
        print("You took too much!")
        dead()
    elif answer < 100:
        print("You made it away safely")
    else:
        print("You took the exact amount to unleash the lions!")
        dead()

def dead():
    print("GAME OVER!")
    exit(0)


start()
