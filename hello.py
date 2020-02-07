def myfunc(word):
    word = word.lower()
    index = 0
    new_string = ""
    for char in word:
        if index % 2 == 0:
            new_string = new_string + char
        else:
            new_string = new_string + char.upper()
        index = index + 1
    return new_string


def yoda(sentence):
    return "mmmmm... " + " ".join(sentence.split()[::-1])


"""
Given a list of ints, return True if the array contains
a 3 next to a 3
"""


def has_33(nums):
    if 3 in nums and nums[-1] is not 3:
        index_of_first_3 = nums.index(3)
        if (nums[index_of_first_3 + 1]) == 3:
            return True
        else:
            return False
    else:
        return False


def paper_doll(string):
    new_string = ''
    for char in string:
        new_string += char*3
    return new_string


def blackjack(a, b, c):
    total = a+b+c
    number_of_aces = list([a, b, c]).count(11)
    if total <= 21:
        return total
    else:
        return (total-10*number_of_aces if number_of_aces in [1, 2, 3] else 'BUST')
