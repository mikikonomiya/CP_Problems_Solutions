'''
You are given two strings s1 and s2.

Return true if s2 contains a permutation of s1, or false otherwise. 
That means if a permutation of s1 exists as a substring of s2, then return true.

Both strings only contain lowercase letters.
'''

##      SLIDING WINDOW

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1):
            return False

        s1_let = [0 * i for i in range(26)]
        for letter in s1:
            s1_let[ord(letter) - ord('a')] += 1

        length = len(s1)
        sub_let = [0 * i for i in range(26)]
        for letter in s2[:length]:
            sub_let[ord(letter) - ord('a')] += 1

        for i in range(len(s2) - length + 1):
            
            if sub_let == s1_let:
                return True
            if i == len(s2) - length:
                return False

            sub_let[ord(s2[i]) - ord('a')] -= 1
            sub_let[ord(s2[i + length]) - ord('a')] += 1
