'''
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise
'''

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        d = {}
        for num in arr:
            if num in d.keys():
                d[num] += 1
            else:
                d[num] = 1
        keys = d.keys()
        occurrences = []
        for key in keys:
            occurrences.append(d[key])
        occurrences1 = list(set(occurrences))
        occurrences.sort()
        occurrences1.sort()
        return occurrences == occurrences1