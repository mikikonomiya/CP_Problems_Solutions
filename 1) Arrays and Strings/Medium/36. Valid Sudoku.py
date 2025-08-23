'''
You are given a 9 x 9 Sudoku board board. 
A Sudoku board is valid if the following rules are followed:

Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.
'''

##      HASHING

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        cols = defaultdict(set)
        rows = defaultdict(set)
        squared = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.' and (board[i][j] in cols[j] or board[i][j] in rows[i] or board[i][j] in squared[(i//3, j//3)]):
                    return False

                cols[j].add(board[i][j])
                rows[i].add(board[i][j])
                squared[(i//3, j//3)].add(board[i][j])
        return True