'''
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.


'''
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        i = 0
        j = len(nums) - 1
        nums.sort()
        counter = 0
        while i < j:
            somma = nums[i] + nums[j]
            if somma > k:
                j -= 1
            elif somma < k:
                i += 1
            else:
                counter += 1
                i += 1
                j -= 1
        return counter