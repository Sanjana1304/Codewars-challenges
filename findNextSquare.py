""" Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. 
Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.
LEVEL : 7kyu """

import math
def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    sqrt = math.sqrt(sq)
    if sqrt==int(sqrt):
        sqrt+=1
        return sqrt**2
    return -1
