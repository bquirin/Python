from sys import argv #python3 -m pydoc (arg) to access pydocs

script, userName, computerName = argv
prompt = "->"

print("Hi {} I'm the {} script".format(userName, script))
print("I'd like to ask you a few questions")
print("Do you like me {}".format(userName))

likes = input(prompt)

print(f"Where do you live {userName}")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
Alright, so you said {!r} about liking me.
You live in {!r}. Not sure where that is.
And you have a {!r} computer called {!r}. Nice.
""".format(likes, lives,computer,computerName))
