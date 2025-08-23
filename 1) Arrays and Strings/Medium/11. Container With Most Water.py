'''
You are given an integer array heights where heights[i] represents the height of the i th bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.
'''

## TWO POINTERS

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        curr_max = 0
        l, r = 0, len(heights) - 1

        while l < r:
            curr_max = max(curr_max, (r - l) * min(heights[l], heights[r]))
            
            if heights[l] < heights[r]:
                l += 1
                continue
            elif heights[l] > heights[r]:
                r -= 1
                continue

            if heights[r-1] > heights[l + 1]:
                r -= 1
            else:
                l += 1
        return curr_max