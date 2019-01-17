def breakWords(stuff):
    """This function will break up words for us"""# Documentation comments
    words = stuff.split(' ')
    return words

def sortWords(words):
    """Sorts the words"""
    return sorted(words)

def printFirstWord(words):
    """Print the first word after popping it off"""
    word = words.pop(0)
    print(word)

def printLastWord(words):
    """Prints the last word affter popping it off"""
    word = words.pop(-1)
    print(word)

def sortSentence(sentence):
    """Takes in a full sentence and returns the sorted word"""
    words = breakWords(sentence)
    return sortWords

def printFirstAndLast(sentence):
    """Prints the first and last words of the sentence"""
    words = breakWords(sentence)
    printFirstWord(words)
    printLastWord(words)

def printFirstAndLastSorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    printFirstWord(words)
    printLastWord(words)
