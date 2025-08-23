'''
Given a binary array nums and an integer k, return the maximum number of consecutive 1's 
in the array if you can flip at most k 0's.

'''

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
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
                if zeros<k:
                    maximum = max(maximum, j+1-i)
                    j+=1
                    zeros += 1
                else:
                    while nums[i]:
                        i+=1
                    i+=1
                    j+=1
        return maximum