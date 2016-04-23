# magic squares 3 x 3

# there are 8 different squares


class square:
    def __init__(self,row1,row2,row3):
        self.row1 = row1
        self.row2 = row2
        self.row3 = row3
        self.col1 = [row1[0],row2[0],row3[0]]
        self.col2 = [row1[1],row2[1],row3[1]]
        self.col3 = [row1[2],row2[2],row3[2]]
        self.matrix = [row1,row2,row3]


    def print_square(self):
        print('\n'.join([''.join(['{:3}'.format(item) for item in row]) for row in self]))



    def rotate_left(self):
        self.col1 = self.row1
        self.col2 = self.row2
        self.col3 = self.row3
        self.matrix


    def rotate_right(self):


    def inverse:




squaress()

squaress = [[8,1,6],[3,5,7],[4,9,2]]
print_square(square)
square = square[::-1][::-1]
print("\n")
print_square(square)


