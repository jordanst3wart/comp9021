# Utility to prompt the user for an integer with a range that can be specified,
# until the user input is of the expected type.
#
# Written by Eric Martin for COMP9021

def input_int(prompt = 'What do you want N to be? ',
                        min_value = float('-inf'), max_value = float('inf')):
    correct_input = False
    while not correct_input:
        input_string = input(prompt)
        try:
            input_value = int(input_string)
            if input_value < min_value or input_value > max_value:
                raise ValueError
            correct_input = True
        except ValueError:
            print('Incorrect input. ', end = '')
    return input_value
