# Prompts the user for an arity N (a nonnegative integer) and a term
# where the function symbols are assumed to consist of nothing but alphabetic
# characters and underscores, with spaces allowed at the beginning
# and around parentheses and commas.
# Checks that the term is syntactically correct according to the definition of a term
# and also in that all function symbols are of arity N or 0.
#
# Written by Foo Bar (Or maybe Jordan Stewart) and Eric Martin for COMP9021


import sys
import re
import unittest


# checks if arity is 0 and calls to other functions
def is_syntactically_correct(term, arity):
    # arity of 0
    if arity == 0:
        if zero_arity(term):
            return True
        else:
            return False

    if no_syntax_errors(term) and no_arity_errors(term,arity):
        return True
    else:
        return False

# arity of 0
def zero_arity(term):
    pattern = re.compile('\s+')
    if pattern.match(term) or term == "":
        return True
    else:
        return False


# checks syntax of arguements
def no_syntax_errors(term):
    # pattern=re.compile('\s*\w+\s*')  #0 or more spaces followed by characters or underscores followed by 0 or more spaces
    pattern=re.compile('\s*[a-zA-Z_)]+\s*')
    found_this = re.split('\,|\(', term)      # split on either , ( )
    for part in found_this:
        if not(pattern.match(part)):  # with a whitespace or something
            return False
    return True


# decoupled logic of arity errors (hopefully decoupled)
def no_arity_errors(term,arity):
    (number_of_open,number_of_closed,number_of_commas) = count_brackets_and_commas(term)
        # unequal brackets
    if(number_of_closed != number_of_open):
        return False

    # no brackets
    if number_of_open == 0:
        return False

    Cn = number_of_commas/number_of_open
    Bn = 1  # number_of_open/number_of_open
    if Cn+Bn==arity:
        return True
    else:
        return False


# checks if the number of brackets and commas is correct
def count_brackets_and_commas(term):
    number_of_open = term.count('(')
    number_of_closed = term.count(')')
    number_of_commas = term.count(',')
    return (number_of_open,number_of_closed,number_of_commas)


# where the func is at
try:
    arity = int(input('Input an arity : '))
    if arity < 0:
        raise ValueError
except ValueError:
    print('Incorrect arity, giving up...')
    sys.exit()
print('A term should contain only letters, underscores, commas, parentheses, spaces.')
term = input('Input a term: ')
if is_syntactically_correct(term, arity):
    print('Good, the term is syntactically correct.')
else:
    print('Unfortunately, the term is syntactically incorrect.')


# test functions
#class TestFunctions(unittest.TestCase):
   # global __testsCases
   # __testCases = [[0, "f_1", False],[1,"f[a]",False],[0,"()",False],[1,"f)",False],
   #             [2, "f(a, g(b))", False],[3,"f((a,b,c))",False],[3,"f(g(a,b,c),g(a,b,c),g(a,b,c)",False],
   #            [3,"f(a, g(a, b, f(a,b,c)), b, c)",False],[0,"",True],[3,"constant",False],[1,"function_of_arity_one(hello)",True],
   #             [0,"function_of_arity_one(hello)",False],[2,"F(g(a,a)), f(a,b))", True],[3,"F(g(a,a)), f(a,b))",False],
   #             [4,"f(a, FF(a, b, fff(a, b, c, FfFf(a,b,c,d)), FfFf(a,b,c,d)), c,d)", True],
   #            [3, "ff(ff(ff(a,b,ff(aa,bb,cc))  ,  b ,  ff(a,b,c))  ,  b  ,  ff(a,ff(a,b,c),c))",True]]

    # count_brackets_and_commas(term,arity):
    #def test_upper(self):
    #    self.assertEqual('foo'.upper(), 'FOO')

    #def test_isupper(self):
    #    self.assertTrue('FOO'.isupper())
    #    self.assertFalse('Foo'.isupper())

    #def test_split(self):
    #    s = 'hello world'
    #    self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
    #    with self.assertRaises(TypeError):
    #        s.split(2)

    #def test_count_brackets_and_commas(self):
        # input brackets
    #    term = "(())"
    #    expected = (2,2,0)
    #    arity = 0
    #    self.assertEqual(count_brackets_and_commas(term), expected)

    # test syntax
    #def test_syntax(self):
    #    self.assertTrue(no_syntax_errors(term))

        # input right and wrong synatx

    #def test_syntax(self):
    #    Stuff = [[0, "f_1", False, True, False],[1,"f[a]",False, False, False],[0,"()",False, True, False],[1,"f)",False, True, False],
    #            [2, "f(a, g(b))", False, True, False],[3,"f((a,b,c))",False, True, False],[3,"f(g(a,b,c),g(a,b,c),g(a,b,c)",False, True, False],
    #            [3,"f(a, g(a, b, f(a,b,c)), b, c)",False, True, False],[0,"",True, True, True],[3,"constant",False, True, False],[1,"function_of_arity_one(hello)",True, True, True],
    #            [0,"function_of_arity_one(hello)",False,True,False],[2,"F(g(a,a), f(a,b))", True, True,True],[3,"f(g(a,a), f(a,b))",False,True,False],
    #            [4,"f(a, FF(a, b, fff(a, b, c, FfFf(a,b,c,d)), FfFf(a,b,c,d)), c,d)", True,True,True],
    #            [3, "ff(ff(ff(a,b,ff(aa,bb,cc))  ,  b ,  ff(a,b,c))  ,  b  ,  ff(a,ff(a,b,c),c))",True,True,True]]

    #    for each in Stuff:
    #        print("got: ", no_syntax_errors(each[1])," answer:", each[3], "with: ", each[1],"\n")
    #        if each[3]:
    #            self.assertTrue(no_syntax_errors(each[1]))
    #        else:
    #            self.assertFalse(no_syntax_errors(each[1]))


    #def test_complete(self):
    #    Stuff = [[0, "f_1", False],[1,"f[a]",False],[0,"()",False],[1,"f)",False],
    #            [2, "f(a, g(b))", False],[3,"f((a,b,c))",False],[3,"f(g(a,b,c),g(a,b,c),g(a,b,c)",False],
    #            [3,"f(a, g(a, b, f(a,b,c)), b, c)",False],[0,"",True],[3,"constant",False],[1,"function_of_arity_one(hello)",True],
    #            [0,"function_of_arity_one(hello)",False],[2,"F(g(a,a)), f(a,b))", True],[3,"F(g(a,a)), f(a,b))",False],
    #            [4,"f(a, FF(a, b, fff(a, b, c, FfFf(a,b,c,d)), FfFf(a,b,c,d)), c,d)", True],
    #            [3, "ff(ff(ff(a,b,ff(aa,bb,cc))  ,  b ,  ff(a,b,c))  ,  b  ,  ff(a,ff(a,b,c),c))",True]]

    #    for each in Stuff:
    #        # print("got: ", is_syntactically_correct(each[1],int(each[0]))," answer:", each[2], "with: ", each[1])
    #        if each[2]:
    #            self.assertTrue(is_syntactically_correct(each[1],int(each[0])))
    #        else:
    #            self.assertFalse(is_syntactically_correct(each[1],int(each[0])))


#if __name__ == '__main__':
    #inputting arguements from the command line
    #if( len(sys.argv) == 2 ):
    #    arg1 = sys.argv[1]
    #    arg2 = sys.argv[2]
    #mainFunc()  # comment to just run tests
    #unittest.main()