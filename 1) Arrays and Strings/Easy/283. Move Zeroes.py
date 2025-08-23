'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
'''

class Solution(object):
    def moveZeroes(self, nums):
        j = 0
        length = len(nums)
        for i in range(length):
            if nums[i] != 0:
                nums[j] = nums[i]
                j+=1
        while j < length:
            nums[j] = 0
            j+=1
        return nums