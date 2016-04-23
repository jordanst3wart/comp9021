


try:
    digits = input("Input a number that represents the desired sum:")
    nb = input("Input a number that represents the desired sum:")
    line = re.sub('\s+', '', line) # remove possible whitespace
    line = list(line)   # make into a list of characters
    # TODO I should check if the values input are numbers
    if len(line)!=8:
        raise ValueError
    for i in line:
        int(i)      # gives up if not an int
    if not(''.join(sorted(line)) == '12345678'):
        raise ValueError
except ValueError:
    print('Incorrect input, giving up...')
    sys.exit()

Input a number that we will use as available digits: 12234
print("Input a number that represents the desired sum:")
5

print("There are",nb ,"solutions.")