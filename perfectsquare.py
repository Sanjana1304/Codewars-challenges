""" Given an integral number, determine if it's a square number """

import math
def is_square(n):
    if n>=0:
        sq = math.sqrt(n)
        if sq==int(sq):
            return True
    return False
