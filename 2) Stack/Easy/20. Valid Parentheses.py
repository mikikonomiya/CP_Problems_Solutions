'''
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {'(':')', '[':']', '{':'}'}
        for letter in s:
            if letter == '(' or letter == '[' or letter == '{':
                stack.append(d[letter])
            else:
                if stack == [] or letter != stack.pop():
                    return False
        if stack == []:
            return True
        return False
