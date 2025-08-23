'''
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.
'''

##      HASHING

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        length = len(nums)
        freq = [[] for i in range(length)]
        s = set(nums)
        
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for num in s:
            freq[count[num]-1].append(num)
        
        result = []
        for i in range(length):
            index = length - 1 - i
            if freq[index] != []:
                result.extend(freq[index])
            if len(result) == k:
                return result