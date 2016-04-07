# Jordan Stewart
# z3291315

# might need to read the text file first

import re
import sys

# build off each letter
# match word in attached text file
# save the highest scoring word and score


# read the file and return the data
def read_file():
    file_name = "wordsEn.txt"
    with open(file_name, "r") as file:      # just read
        content = file.readlines()          # from http://stackoverflow.com/questions/3277503/python-read-file-line-by-line-into-array
    file.close()                            # close the file
    return content


def find_highest_scoring_words(line,file_data):
    best_words = []           # no words found
    score = 0
    letters = list(line)
    letters = sorted(letters)
    # loop start here, finish when all letter combos check

    # create letter combination in alphabertical order
    # TODO I actually need to write this.
    words = create_word_combos(letters)

    # for each word
    # check if word is in the file_data
    for word in words:
        # TODO I actually need to write this aswell.
        if is_word(word,file_data):
            temp = score_word(word)      # score word
            if temp >= score:            # I should make this if statement better
                score = temp                # if score higher save word and score as new high score
                best_words.append(word)

    return [best_words, score]


# letters are sorted
def create_word_combo(letters):
    word_combos = ["word1","word2"]  # in alphabert
    return word_combos




def is_word(word,file_data):
    return True



# might need refactoring
# return true if word is matched with the letters
def match_word_from_letters(letters, word):
    list_word = list(word)
    return compare(letters,list_word)


# compare to lists. Thanks stack http://stackoverflow.com/questions/7828867/how-to-efficiently-compare-two-unordered-lists-not-sets-in-python
def compare(list1, list2):
    return sorted(list1) == sorted(list2)


# given word return score
def score_word(word):
    score = 0
    # dictionary values
    values = {'a': 2, 'b': 5,'c':4,'d':4,'e':1,'f':6,
       'g':5, 'h':5, 'i':1, 'j':7, 'k':6, 'l':3,
       's':1, 't':2, 'u':4, 'v':6, 'w':6, 'x':7,
        'y':5, 'z':7}
    word_list=list(word)
    for letter in word_list:
        score += values[letter]
    return score


# prints the output
def message_function(words, score):
    if len(words) == 0:
        print("No word is built from some of those letters.")
    elif len(words) == 1:
        print("The highest score is ", score,".")
        print("The highest scoring word is ", words[0])
    else:
        # if multiple
        # for each word print
        print("The highest scoring words are, in alphabetical order: ")
        print_multiple_words(words)


# prints words assuming they are in alphabertical order
def print_multiple_words(words):
    # sort to be in alphabert
    for word in words:
        print(word)


# import text file document with try
try:
    line = input("Enter between 3 and 10 lowercase letters: ")
    line = re.sub('\s+', '', line)  # remove possible whitespace, used in rubik as well
    line = list(line)               # make into a list of characters
    # TODO raise error for numbers or weird stuff in input. Make sure it is a char.
    if len(line) < 3 or len(line) > 10:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up...')
    sys.exit()

#value = calculate_number_of_steps(line)
#print(value, 'steps are needed to reach the final configuration.')

file_data = read_file()
[words, score] = find_highest_scoring_words(line, file_data)
message_function(words,score)





