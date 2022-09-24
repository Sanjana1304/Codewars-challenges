"""
In this kata you have to create all permutations of a non empty input string and remove duplicates, if present. 
This means, you have to shuffle all letters from the input in all possible orders.

Examples:

* With input 'a'
* Your function should return: ['a']
* With input 'ab'
* Your function should return ['ab', 'ba']
* With input 'aabb'
* Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']

LEVEL : 4kyu
"""

l=[]
def toString(List):
    x= ''.join(List)
    l.append(x)

def permute(a,start,end):
    if start==end:
        toString(a)      
    else:
        for i in range(start,end+1):
            a[start],a[i] = a[i],a[start]
            permute(a,start+1,end)
            a[start],a[i] = a[i],a[start]

def permutations(s):
    a=list(s)
    permute(a,0,len(s)-1)
    m=[]
    for i in list(set(l)):
        if len(i)==len(s):
            m.append(i)
    l.clear()
    return m

