'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.
'''

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        i = 0
        length = len(s)
        while i < length:
            string = ''
            number = ''
            if s[i] != ']':
                stack.append(s[i])
            else:
                while stack[-1].isalpha():
                    string = stack.pop() + string
                stack.pop()
                while len(stack) != 0 and stack[-1].isnumeric():
                    number = stack.pop() + number
                if number != '':
                    string *= int(number)
                stack.append(string)
            i += 1
        return ''.join(stack)
        