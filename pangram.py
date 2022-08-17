""" A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

LEVEL : 6kyu """

def is_pangram(s):
    s=s.upper()
    alpha=dict()
    
    for i in range(65,91):
        alpha[chr(i)] = 0
    
    for i in s:
        if i in alpha.keys():
            alpha[i] = 1
    cnt=0
    for i in alpha.values():
        if i==1:
            cnt+=1
    if cnt==26:
        return True
    return False
