# Jordan Stewart
# z3291315

# might need to read the text file first

import re
import sys
import itertools
import math

# build off each letter
# match word in attached text file
# save the highest scoring word and score


# read the file and return the data
def read_file():
    file_name = "wordsEn.txt"
    with open(file_name, "r") as file:      # just read
        content = file.read().splitlines() # readlines()          # from http://stackoverflow.com/questions/3277503/python-read-file-line-by-line-into-array
    file.close()                            # close the file
    return content


# creates a dictionary with unique letter combinations being the key
def create_dict():
    content = read_file()
    dict_of_words = dict()
    for word in content:
        letters=list(word)
        letters.sort()
        letters = ''.join(letters) # concat letters to string
        if letters in dict_of_words.keys():
            dict_of_words[letters].append(word)
        else:
            dict_of_words[letters] = [word]
    #print('Lines in file: ',len(content), 'dictionary items: ', len(dict_of_words))
    return dict_of_words


def find_highest_scoring_words(line, list_of_words):
    letters = list(line)
    letters = sorted(letters)
    # create letter combination in alphabertical order
    # if not enough memory I could create words of different lengths
    combinations = create_word_combos(letters)         # letters! number of words created
    words = is_word(combinations, list_of_words)
    [words, score] = sort_words(words)
    return [words, score]


# letters are sorted
# max length of combos is n! if duplicates included
# iterates for lengths of words and creates combinations, no duplicate letter combinations
def create_word_combos(letters):
    word_combos = []
    for L in range(1, len(letters)+1):
        for subset in itertools.combinations(letters, L):
            subset = ''.join(subset) # concat letters to string
            word_combos.append(subset)
    word_combos=set(word_combos) # removes duplicates with shared letters ie. aaa returns 'a', 'aa', 'aaa' rather than 'a', 'aa', 'aa' etc
    # print("max combos: ", math.factorial(len(letters)),"actual combos: ", len(word_combos))
    return word_combos


# checks if words are in the list_of_words
def is_word(combinations,list_of_words):
    new_list_of_words = []
    for combo in combinations:
        if combo in list_of_words:
            new_list_of_words.append(combo)

    return new_list_of_words


def sort_words(words):
    highest_score = 0
    new_list = []
    for word in words:
        score = score_word(word)
        if score > highest_score:
            highest_score = score
            new_list = []
            new_list.append(word)
        elif score == highest_score:
            new_list.append(word)

    return [new_list, highest_score]


# given word return score
def score_word(word):
    score = 0
    # dictionary values
    values = {'a': 2, 'b': 5,'c':4,'d':4,'e':1,'f':6,
        'g':5, 'h':5, 'i':1, 'j':7, 'k':6, 'l':3,
        'm': 5,'n':2,'o':3,'p':5,'q':7,'r':2,
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

#dict_of_words = read_file()
dict_of_words = create_dict()

#[words, score] = find_highest_scoring_words(line, dict_of_words)
#message_function(words,score)

