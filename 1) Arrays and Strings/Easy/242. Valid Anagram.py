'''
Given two strings s and t, return true if the two strings are anagrams 
of each other, otherwise return false.
An anagram is a string that contains the exact same characters as another 
string, but the order of the characters can be different.
'''

##      HASHING

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        for val in count:
            if val != 0:
                return False
        return True