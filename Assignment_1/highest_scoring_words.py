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
        content = file.read().splitlines()  # from http://stackoverflow.com/questions/3277503/python-read-file-line-by-line-into-array
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


def find_highest_scoring_words(line, dict_of_words):
    letters = list(line)
    letters = sorted(letters)
    # create letter combination in alphabertical order
    # if not enough memory I could create words of different lengths
    combinations = create_word_combos(letters)         # letters! number of words created
    list_of_list_of_words = find_words(combinations, dict_of_words)
    [list_of_list_of_words, score] = sort_words(list_of_list_of_words)
    return [list_of_list_of_words, score]


# letters are sorted
# max length of combos is n! if duplicates included
# iterates for lengths of words and creates combinations, no duplicate letter combinations
def create_word_combos(letters):
    word_combos = []
    for L in range(1, len(letters)+1):
        for subset in itertools.combinations(letters, L):
            subset = list(subset)                # change from tuple to list
            subset.sort()               # sorts the letters in alphabetical order
            subset = ''.join(subset)    # concat letters to string
            word_combos.append(subset)
    word_combos=set(word_combos) # removes duplicates with shared letters ie. aaa returns 'a', 'aa', 'aaa' rather than 'a', 'aa', 'aa' etc
    # print("max combos: ", math.factorial(len(letters)),"actual combos: ", len(word_combos))
    return word_combos


# checks if letters are in the dict_of_words
def find_words(combinations, dict_of_words):
    new_list_of_words = []
    for combo in combinations:
        if combo in dict_of_words:
            new_list_of_words.append(dict_of_words[combo])
    return new_list_of_words


# all the words in the list now have the same score unless there is two lists
# finds the list with the highest score
def sort_words(list_of_list_of_words):
    highest_score = 0
    new_list = []
    for list_of_words in list_of_list_of_words:
        score = score_word(list_of_words[0])
        if score > highest_score:
            highest_score = score
            new_list = []
            new_list.append(list_of_words)
        elif score == highest_score:
            new_list.append(list_of_words)

    # flattening the list
    flattened = []
    if any(isinstance(el, list) for el in new_list):
        for sublist in new_list:
            for val in sublist:
                flattened.append(val)

    return [flattened, highest_score]


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
        #print(score,".")
        sys.stdout.write("The highest score is ")
        sys.stdout.write(str(score))
        sys.stdout.write(".\n") # to remove that annoying space
        print("The highest scoring word is", words[0])
    else:
        # if multiple
        # for each word print
        sys.stdout.write("The highest score is ")
        sys.stdout.write(str(score))
        sys.stdout.write(".\n") # to remove that annoying space
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
    for letter in line:
        if not(letter.isalpha()):
            raise ValueError
except ValueError:
    print('Incorrect input, giving up...')
    sys.exit()

#value = calculate_number_of_steps(line)
#print(value, 'steps are needed to reach the final configuration.')

#dict_of_words = read_file()
dict_of_words = create_dict()

[words, score] = find_highest_scoring_words(line, dict_of_words)
words=sorted(words)
message_function(words,score)

