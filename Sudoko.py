"""Write a function done_or_not/DoneOrNot passing a board (list[list_lines]) as parameter.
If the board is valid return 'Finished!', otherwise return 'Try again!' 
Rule 1: There are 9 rows in a traditional Sudoku puzzle. Every row must contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9. 
There may not be any duplicate numbers in any row. In other words, there can not be any rows that are identical.


Rule 2: There are 9 columns in a traditional Sudoku puzzle. Like the Sudoku rule for rows, every column must also contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9. 
Again, there may not be any duplicate numbers in any column. Each column will be unique as a result.

Rule 3: A region is a 3x3 box like the one shown to the left. There are 9 regions in a traditional Sudoku puzzle.

Like the Sudoku requirements for rows and columns, every region must also contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9. 
Duplicate numbers are not permitted in any region. Each region will differ from the other regions.

LEVEL : 5kyu
"""

#This code is incomplete. Its under working
def done_or_not(board): #board[i][j]
    con=0 #total 3 conditions
    
    #checking rows
    row_cnt=0 
    for i in board:
        if 1 in i and 2 in i and 3 in i and 4 in i and 5 in i and 6 in i and 7 in i and 8 in i and 9 in i:
            row_cnt+=1
    if row_cnt==9:
        con+=1
    
    #coverting columns to rows
    column_list=[]  
    for i in range(0,9):
        l=[]
        for j in range(0,9):
            l.append(board[j][i])
        column_list.append(l)
    
    #checking columns
    col_cnt=0
    for i in column_list:
        if 1 in i and 2 in i and 3 in i and 4 in i and 5 in i and 6 in i and 7 in i and 8 in i and 9 in i:
            col_cnt+=1
    if col_cnt==9:
        con+=1
  # your solution here
  # ..
  # return 'Finished!'
  # ..
  # or return 'Try again!'
