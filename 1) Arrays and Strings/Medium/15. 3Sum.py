'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, 
and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.
'''

##      TWO POINTERS

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, num in enumerate(nums):
            if num > 0:
                break

            if i > 0 and num == nums[i - 1]:
                continue

            index1, index2 = i + 1, len(nums) - 1

            while index1 < index2:
                threeSum = num + nums[index1] + nums[index2]
                if threeSum == 0:
                    res.append([num, nums[index1], nums[index2]])
                    index1 += 1
                    while nums[index1] == nums[index1 - 1] and index1 < index2:
                        index1 += 1
                elif threeSum > 0:
                    index2 -= 1
                else:
                    index1 += 1
        
        return res