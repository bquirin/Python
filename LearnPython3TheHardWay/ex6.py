x = "There are {!a} types of people".format(10)
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}"

print(x)
print(y)

print(f"I said {x!r}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right string"

print(w + e)

print ''.join((w,e))
