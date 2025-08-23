'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
'''

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = []
        for letter in s:
            if letter in 'aeiouAEIOU':
                vowels.append(letter)
        new_string = list(s)
        counter = 0
        for i, letter in enumerate(new_string):
            if letter in 'aeiouAEIOU':
                new_string[i] = vowels[-(counter + 1)]
                counter += 1
        return ''.join(new_string)