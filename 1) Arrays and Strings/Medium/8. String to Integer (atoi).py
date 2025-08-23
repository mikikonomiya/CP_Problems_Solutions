'''
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. 
            If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], then round the integer to remain in the range. 
            Specifically, integers less than -2^31 should be rounded to -2^31, and integers greater than 2^31 - 1 should be rounded to 2^31 - 1.
Return the integer as the final result.
'''

## 

class Solution:
    def myAtoi(self, s: str) -> int:
        number = ""
        isNeg = False
        
        if s == '':
            return 0

        if s[0] == ' ':
            while s!= '' and s[0] == ' ':
                s = s[1:]
            if s == '':
                return 0

        if s[0] in {"+", "-"}:
            if s[0] == "-":
                isNeg = True
            s = s[1:]
            if s == '':
                return 0

        if s[0] == 0:
            while s!= '' and s[0] == 0:
                s = s[1:]
            if s == '':
                return 0

        if s[0] not in {"1","2","3","4","5","6","7","8","9","0"}:
            return 0

        while s != '' and s[0] in {"1","2","3","4","5","6","7","8","9","0"}:
            number += s[0]
            s = s[1:]

        result = int(number)
        if isNeg:
            result = 0-result

        if result > 2**31 -1:
            result = 2**31 -1

        if result < -2**31:
            result = -2**31

        return result