'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the 
value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        string = str(x)
        # check sign
        isNeg = False
        if string[0] == '-':
            isNeg = True
            string = string[1::]

        # check zeros
        while string[-1] == '0':
            if string == '0':
                return 0
            string = string[:-1]

        string = string[::-1]

        if isNeg:
            string = '-' + string
            
        # check size
        if int(string) > 2147483646 or int(string) < -2147483647:
            return 0
        
        return int(string)