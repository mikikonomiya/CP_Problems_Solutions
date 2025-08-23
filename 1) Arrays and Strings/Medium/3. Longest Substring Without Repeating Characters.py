'''
Given a string s, find the length of the longest substring without duplicate characters.
A substring is a contiguous sequence of characters within a string.
'''

##      SLIDING WINDOW

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        if len(s) == 1:
            return 1

        letters = {s[0]}
        l, r = 0, 1
        max_len = 0

        while r < len(s):
            if s[r] not in letters:
                letters.add(s[r])
                r += 1
            else:
                letters.remove(s[l])
                l += 1
            max_len = max(max_len, len(letters))
        return max_len
            