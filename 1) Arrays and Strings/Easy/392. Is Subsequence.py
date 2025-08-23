'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) 
of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence 
of "abcde" while "aec" is not).
'''

class Solution(object):
    def isSubsequence(self, s, t):
        i = 0
        j = 0
        len_s = len(s)
        len_t = len(t)
        while i < len_s and j < len_t:
            if t[j] == s[i]:
                i += 1
            j += 1
        if i == len_s:
            return True
        return False