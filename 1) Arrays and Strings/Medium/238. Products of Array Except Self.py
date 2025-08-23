'''
Given an integer array nums, return an array output where output[i] 
is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in 
O(n) time without using the division operation?
'''
##      Prefix & Suffix

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [1]
        i = 1
        length = len(nums)

        while i < length:
            prefix.append(prefix[-1] * nums[i-1])
            i += 1
        
        i -= 1
        suffix = [1]
        while i > 0:
            suffix.append(suffix[-1] * nums[i])
            i -= 1
        
        return [prefix[i]*suffix[-(1+i)] for i in range(len(nums))]
