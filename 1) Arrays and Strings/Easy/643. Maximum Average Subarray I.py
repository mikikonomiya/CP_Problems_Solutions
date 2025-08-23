'''
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10^-5 will be accepted.
'''

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        i = 0
        length = len(nums)
        array = [sum(nums[:k])]
        while i + k < length:
            array.append(array[-1] - nums[i] + nums[i+k])
            i += 1
        maximum = max(array)
        return float(maximum) / float(k)