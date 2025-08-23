'''
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
'''

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        length = len(s)//2
        counter = 0
        while length > 0:
            val = s[counter]
            s[counter] = s[-counter-1]
            s[-counter-1] = val
            length -= 1
            counter += 1
        return s