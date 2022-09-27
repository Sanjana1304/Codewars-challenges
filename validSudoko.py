"""
Write a function done_or_not/DoneOrNot passing a board (list[list_lines]) as parameter. 
If the board is valid return 'Finished!', otherwise return 'Try again!'

Sudoku rules:
Complete the Sudoku puzzle so that each and every row, column, and region contains the numbers one through nine only once.

RULE 1:
There are 9 rows in a traditional Sudoku puzzle. Every row must contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9. 
There may not be any duplicate numbers in any row. In other words, there can not be any rows that are identical.

RULE 2:
There are 9 columns in a traditional Sudoku puzzle. Like the Sudoku rule for rows, every column must also contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9. 
Again, there may not be any duplicate numbers in any column. Each column will be unique as a result.

RULE 3:
A region is a 3x3 box like the one shown to the left. There are 9 regions in a traditional Sudoku puzzle.

Like the Sudoku requirements for rows and columns, every region must also contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9.
Duplicate numbers are not permitted in any region. Each region will differ from the other regions.

LEVEL : 5kyu 

SAMPLE TEST CASE:
board = [[5, 3, 4, 6, 7, 8, 9, 1, 2], 
         [6, 7, 2, 1, 9, 5, 3, 4, 8],
         [1, 9, 8, 3, 4, 2, 5, 6, 7],
         [8, 5, 9, 7, 6, 1, 4, 2, 3],
         [4, 2, 6, 8, 5, 3, 7, 9, 1],
         [7, 1, 3, 9, 2, 4, 8, 5, 6],
         [9, 6, 1, 5, 3, 7, 2, 8, 4],
         [2, 8, 7, 4, 1, 9, 6, 3, 5],
         [3, 4, 5, 2, 8, 6, 1, 7, 9]]  (Its a finished and valid board)
         
board = [[1, 3, 2, 5, 7, 9, 4, 6, 8]
        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
        ,[8, 7, 9, 6, 4, 2, 1, 3, 5]] (Its an invalid board)

"""

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
        
    #creating region lists
    b=[]
    for i in board:
        l=[]
        for j in range(0,10,3):
            if i[j:j+3]!=[]:
                l.append(i[j:j+3])
        b.append(l)

    box1 = b[0][0]
    box1.extend(b[1][0])
    box1.extend(b[2][0])

    box2 = b[0][1]
    box2.extend(b[1][1])
    box2.extend(b[2][1])

    box3 = b[0][2]
    box3.extend(b[1][2])
    box3.extend(b[2][2])

    box4 = b[3][0]
    box4.extend(b[4][0])
    box4.extend(b[5][0])

    box5 = b[3][1]
    box5.extend(b[4][1])
    box5.extend(b[5][1])

    box6 = b[3][2]
    box6.extend(b[4][2])
    box6.extend(b[5][2])

    box7 = b[6][0]
    box7.extend(b[7][0])
    box7.extend(b[8][0])

    box8 = b[6][1]
    box8.extend(b[7][1])
    box8.extend(b[8][1])

    box9 = b[6][2]
    box9.extend(b[7][2])
    box9.extend(b[8][2])

    regions = []
    regions.append(box1)
    regions.append(box2)
    regions.append(box3)
    regions.append(box4)
    regions.append(box5)
    regions.append(box6)
    regions.append(box7)
    regions.append(box8)
    regions.append(box9)
    
    #checking regions
    reg_cnt=0 
    for i in regions:
        if 1 in i and 2 in i and 3 in i and 4 in i and 5 in i and 6 in i and 7 in i and 8 in i and 9 in i:
            reg_cnt+=1
    if reg_cnt==9:
        con+=1
    
    if con==3:
        return 'Finished!'
    return 'Try again!'
