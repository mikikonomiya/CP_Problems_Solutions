'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = 0
        min_len = len(strs[0])
        for word in strs:
            min_len=min(min_len, len(word))
        if min_len == 0:
            return ''
        
        first_let = strs[0][0]
        for word in strs:
             if word[0] != first_let:
                  return ''
             
        while longest <= min_len:
            for word in strs:
                if not word.startswith(strs[0][:longest]):
                    return strs[0][:longest-1]
            longest += 1
        longest -= 1
        return strs[0][:longest]