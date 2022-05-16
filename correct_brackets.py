
'''
This function takes a string including some brackets and 
checks if brackets are correct in the string.
If there they're correct then returns 1, else returns 0.
'''

import re


def verify(string_in: str) -> int:
    brackets = ('()', '[]', '<>')

    if not any(q in string_in for q in [x for l in brackets for x in l]):
        return 1
# Here  [ x for l in brackets for x in l ]  generates  [ '[',']','<','>','(',')' ]

    for b in brackets:
        u = re.search(rf'{re.escape(b[0])}.*{re.escape(b[1])}', string_in)
        if u: return verify(u.group()[1:-1])
    return 0


print(verify("---(++++)----"))  # returns 1
print(verify(""))  # returns 1
print(verify("before ( middle [jghk]) after "))  # returns 1
print(verify(") ("))  # returns 0
print(verify("<(   >)"))  # returns 0
print(verify("(  [  <>  ()  ]  <>  )"))  # returns 1
print(verify("   (      [)"))  # returns 0
