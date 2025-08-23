'''

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the 
left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left.
 This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

 '''

##      PREFIX SUM

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        i = 1
        rightSum = []
        leftSum = []

        leftSum.append(0)
        while i < length:
            leftSum.append(leftSum[-1] + nums[i-1])
            i += 1
            
        i = 1
        nums = nums[::-1]
        rightSum.append(0)
        while i < length:
            rightSum.append(rightSum[-1] + nums[i-1])
            i += 1
        rightSum = rightSum[::-1]
        
        i = 0
        while i < length:
            if rightSum[i] == leftSum[i]:
                return i
            i += 1
        return -1