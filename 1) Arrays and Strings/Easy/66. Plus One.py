'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
'''

class Solution(object):
    def plusOne(self, digits):
        string = ''
        for digit in digits:
            string += str(digit)
        number = int(string)
        number += 1
        string = str(number)
        result = []
        for digit in string:
            result.append(int(digit))
        return result