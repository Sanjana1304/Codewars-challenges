""" Count the number of Duplicates:
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than 
once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits. """

def duplicate_count(text):
    text=text.lower()
    distinct =[]
    for i in text:
        if i not in distinct:
            distinct.append(i)
    total_count=0
    alpha_count=0
    for i in distinct:
        alpha_count = text.count(i)
        if alpha_count>1:
            total_count+=1
    return total_count
