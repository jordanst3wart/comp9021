import unittest
import tangram


# use
# python3 micro_tests.py Q1
# python3 tests.py Q2
# python3 tests.py Q1 Q3

class Q1(unittest.TestCase):

    def test_are_valid(self):
        from tangram import *
        file = open('pieces_A.xml')
        coloured_pieces = available_coloured_pieces(file)
        #self.assertTrue(are_valid(coloured_pieces))
        file = open('pieces_AA.xml')
        coloured_pieces = available_coloured_pieces(file)
        #self.assertTrue(are_valid(coloured_pieces))
        file = open('incorrect_pieces_2.xml')
        coloured_pieces = available_coloured_pieces(file)
        #self.assertFalse(are_valid(coloured_pieces))
        file = open('incorrect_pieces_3.xml')
        coloured_pieces = available_coloured_pieces(file)
        #self.assertFalse(are_valid(coloured_pieces))
        file = open('incorrect_pieces_4.xml')
        coloured_pieces = available_coloured_pieces(file)
        #self.assertFalse(are_valid(coloured_pieces))



# if is run directly
if __name__ == '__main__':
    unittest.main()