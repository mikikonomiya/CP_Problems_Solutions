'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start_row = 0
        end_row = len(matrix) - 1

        while end_row >= start_row:
            midpoint_row = (end_row + start_row) // 2

            if matrix[midpoint_row][0] > target:
                end_row = midpoint_row - 1
            elif matrix[midpoint_row][-1] < target:
                start_row = midpoint_row + 1
            else:
                break

        if end_row < start_row:
            return False
        
        start = 0
        end = len(matrix[0])
        while start <= end:
            midpoint = (end + start) // 2

            if matrix[midpoint_row][midpoint] < target:
                start = midpoint + 1
            elif matrix[midpoint_row][midpoint] > target:
                end = midpoint - 1
            else:
                return True
        return False