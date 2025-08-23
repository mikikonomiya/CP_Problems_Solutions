'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        c = 0
        while True:
            if haystack.startswith(needle):
                return c
            c += 1
            haystack = haystack[1:]