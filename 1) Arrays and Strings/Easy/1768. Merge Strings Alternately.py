'''
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, 
starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
'''

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        len_word1 = len(word1)
        len_word2 = len(word2)
        merged_string = ''
        if len_word1 >= len_word2:
            for index_letter in range(len_word2):
                merged_string += word1[index_letter] + word2[index_letter]
            merged_string += word1[len_word2::]
        else:
            for index_letter in range(len_word1):
                merged_string += word1[index_letter] + word2[index_letter]
            merged_string += word2[len_word1::]
        return merged_string

        