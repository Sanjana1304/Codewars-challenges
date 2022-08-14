""" Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. 
Additionally, if the number is negative, return 0 (for languages that do have them). 
LEVEL : 6kyu """

def solution(number):
    sum=0
    for i in range(number):
        if(i%3==0 or i%5==0):
            sum+=i
    return sum
  
