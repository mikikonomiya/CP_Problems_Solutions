'''
Given an array of strings strs, group all anagrams together into sublists. 
You may return the output in any order.
An anagram is a string that contains the exact same characters as 
another string, but the order of the characters can be different.
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for string in strs:
            l = [0] * 26

            for letter in string:
                l[ord(letter) - ord('a')] += 1
            
            hashmap[tuple(l)].append(string)

        return list(hashmap.values())