# instantiate = create
# instantiate a class you get an object
# self means the instances attribute

class Song(object):
    def __init__(self,lyrics): # the init function is called as soon as the obj is created
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

bump_and_grind = Song(["I don't see nothing wrong",
                       "With a little bump and grind"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

bump_and_grind.sing_me_a_song()
