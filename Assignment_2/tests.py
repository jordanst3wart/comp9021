import unittest
import tangram


# use
# python3 tests.py Q1
# python3 tests.py Q2
# python3 tests.py Q1 Q3
# python3 tests.py


class Q1(unittest.TestCase):

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    #### main functions
    #available_coloured_pieces(file)
    # parse the file
    def test_parse_file(self):
        file = open('pieces_A.xml')
        pieces = available_coloured_pieces(file)
        pass

    # test if input is valid
    def test_is_input_valid(self):
        file = open('pieces_A.xml')
        available_coloured_pieces(file)
        # might need to be tangram.available_coloured_pieces
        pass

    #### minor functions
    # test if three sides

    # test if no interior angle greater than 180

    # test if clockwise of anti clockwise



    # test if


class Q2(unittest.TestCase):

    def PrintHello(self):
        print("hello from two")


class Q3(unittest.TestCase):

    def PrintHello(self):
        print("hello from three")

    #is_solution(tangram , shape)


# if is run directly
if __name__ == '__main__':
    unittest.main()
