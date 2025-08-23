'''
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).
'''

class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        d = {}
        length = len(grid)
        for r, row in enumerate(grid):
            tup = tuple(row)
            if tup not in d.keys():
                d[tup] = 1
            else:
                d[tup] += 1
        list_columns =  [[grid[j][i] for j in range(length)] for i in range(length-1,-1,-1)][::-1]
        columns = []
        for col in list_columns:
            columns.append(tuple(col))
        counter = 0
        for col in columns:
            if col in d.keys():
                counter += d[col]
        return counter