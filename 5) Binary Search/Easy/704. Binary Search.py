'''
You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

Your solution must run in O(logn) time.
'''
def search(nums, target) :
    start, end = 0, len(nums) - 1

    while end >= start:
        midpoint = start + ((end - start)//2)

        if nums[midpoint] > target:
            end = midpoint - 1
        elif nums[midpoint] < target:
            start = midpoint + 1
        else:
            return midpoint
    return -1
