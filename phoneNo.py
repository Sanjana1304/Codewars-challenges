""" Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
LEVEL : 6kyu
 """"

def create_phone_number(n):
    m=[]
    for i in n:
        j = str(i)
        m.append(j)
    x = "".join(m[0:3])
    y= "".join(m[3:6])
    z="".join(m[6:])
    ans = "("+x+") "+y+"-"+z
    return ans
