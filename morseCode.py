""" In this kata you have to write a simple Morse code decoder. While the Morse code is now mostly superseded by voice and digital data 
communication channels, it still has its use in some applications around the world.
The Morse code encodes every character as a sequence of "dots" and "dashes". 
For example, the letter A is coded as ·−, letter Q is coded as −−·−, and digit 1 is coded as ·−−−−. 
The Morse code is case-insensitive, traditionally capital letters are used. When the message is written in Morse code, a single space is 
used to separate the character codes and 3 spaces are used to separate words. 
For example, the message HEY JUDE in Morse code is ···· · −·−−   ·−−− ··− −·· ·.

NOTE: Extra spaces before or after the code have no meaning and should be ignored.

The Morse code table is preloaded for you as a dictionary, feel free to use it:

Coffeescript/C++/Go/JavaScript/Julia/PHP/Python/Ruby/TypeScript: MORSE_CODE['.--']

LEVEL : 6kyu """

def decode_morse(morse_code):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    morse_code = morse_code.split('   ')
    lis = []
    for i in morse_code:
        i=i.split()
        lis.append(i)
    ans = ""
    for i in lis:
        for j in i:
            j=j.replace(j,MORSE_CODE[j])
            ans+=j
        ans+=" "
    ans=ans.strip()
    return ans[:]
