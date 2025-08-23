'''
Given a string s, find the first non-repeating character in it and return its index. 
If it does not exist, return -1.
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        all_letters = set(s)
        for letter in s:
            if letter in all_letters:
                if s.count(letter) == 1:
                    return s.index(letter)
                all_letters.remove(letter)
        return -1