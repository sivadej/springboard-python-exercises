def print_upper_words(words):
    """Docstrings always use triple quotes"""
    for word in words:
        print (word.upper())

# print_upper_words(["hello", "hey", "goodbye", "yo", "yes", "eyy"])

def upper_only_e(words):
    for word in words:
        if word[0] == 'e' or word[0] == 'E':
            print_upper_words(word)

#upper_only_e(["hello", "Ehey", "goodbye", "yo", "yes", "eyy"])

def upper_starts_with(words, must_start_with):
    for letter in must_start_with:
        for word in words:
            if word[0] == letter:
                print(word)

upper_starts_with(["hello", "xxx", "goodbye", "yo", "yes", "eyy"], {"g","h","e"})