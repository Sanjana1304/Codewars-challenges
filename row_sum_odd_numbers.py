""" Given the triangle of consecutive odd numbers:
             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
  Calculate the sum of the numbers in the nth row of this """

def row_sum_odd_numbers(n):
    prev_row_end=0
    for i in range(1,n):
        for j in range(1,i+1):
            prev_row_end+=2
    prev_row_end-=1
    
    curr_row_end=0
    for i in range(1,n+1):
        for j in range(1,i+1):
            curr_row_end+=2
    curr_row_end-=1
    
    sum=0
    for i in range(prev_row_end+2,curr_row_end+1,2):
        sum+=i
    
    return sum
    
