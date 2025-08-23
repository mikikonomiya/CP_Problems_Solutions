'''
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n 
new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
'''

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0: 
            return True
        if len(flowerbed) == 1:
            if n == 1 and flowerbed[0] == 0:
                return True
            else:
                return False
        i = 0
        length = len(flowerbed)
        counter = 0
        while i < length:
            if flowerbed[i] == 0:
                if i == 0:
                    if not flowerbed[i + 1]:
                        counter += 1 
                        i += 2
                    else:
                        i += 1
                elif i == length - 1:
                    if not flowerbed[i - 1]:
                        counter += 1 
                        i += 1
                    else:
                        i += 1
                else:
                    if not flowerbed[i - 1] and not flowerbed[i + 1]:
                        counter += 1 
                        i += 2
                    else:
                        i += 1
            else:
                i += 2
        return n <= counter