""" Complete the solution so that it splits the string into pairs of two characters. 
If the string contains an odd number of characters then it should replace the missing second character 
of the final pair with an underscore ('_').

LEVEL : 6kyu
"""

def solution(s):
    l=[]
    if len(s)%2==0:
        for i in range(0,len(s),2):
            l.append(s[i]+s[i+1])
    else:
        s=s+"_"
        for i in range(0,len(s),2):
            l.append(s[i]+s[i+1])
    return l
            
