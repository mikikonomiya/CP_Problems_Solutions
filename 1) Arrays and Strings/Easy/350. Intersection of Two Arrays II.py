'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must 
appear as many times as it shows in both arrays and you may return the result in any order.
'''

class Solution(object):
    def intersect(self, nums1, nums2):
        result = []
        for el in nums1:
            if el in nums2:
                result.append(el)
                nums2.remove(el)
        return result
        