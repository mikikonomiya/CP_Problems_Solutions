'''
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) 
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, 
or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            m = (end + start) // 2
            if target == nums[m]:
                return m

            if nums[start] <= nums[m]: # im on the left side
                
                if target > nums[m] or target < nums[start]:
                    start = m + 1
                else:
                    end = m - 1

            else: # im on the right side
                if target < nums[m] or target > nums[end]:
                    end = m - 1
                else:
                    start = m + 1
        return -1

