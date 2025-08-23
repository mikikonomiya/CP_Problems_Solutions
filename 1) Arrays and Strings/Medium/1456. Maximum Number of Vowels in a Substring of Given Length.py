'''
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
'''

class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        initial = s[:k]
        n_vowels = 0
        for letter in initial:
            if letter in 'aeiou':
                n_vowels += 1
        i = 1
        length = len(s)
        maximum = n_vowels
        while i + k <= length:
            if s[i+k-1] in 'aeiou':
                n_vowels += 1
            if s[i-1] in 'aeiou':
                n_vowels -= 1
            maximum = max(maximum, n_vowels)
            i += 1
        return maximum