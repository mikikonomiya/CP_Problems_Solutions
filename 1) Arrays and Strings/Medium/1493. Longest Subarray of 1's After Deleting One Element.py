'''
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
'''

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0
        j = 0
        maximum = 0
        length = len(nums)
        zeros = 0
        while j<length:
            if nums[j]:
                maximum = max(maximum, j+1-i)
                j+=1
            else:
                if zeros<1:
                    maximum = max(maximum, j+1-i)
                    j+=1
                    zeros += 1
                else:
                    while nums[i]:
                        i+=1
                    i+=1
                    j+=1
        return maximum-1