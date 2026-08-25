class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        valid: no row and column duplicates
        valid: 3 x 3 grid should not have duplicates

        set() -> hashsets with only one key

        *rowSet -> 1...n
        *columnSet -> 1...m
        *3x3Set -> left, right, up, down, diagonals(4) = 8 total

        3 for loops:

        O(3*n) Time complexity

        """

        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        gridSet = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rowSet[r]
                    or board[r][c] in colSet[c]
                    or board[r][c] in gridSet[(r // 3, c // 3)]):
                    return False

                colSet[c].add(board[r][c])
                rowSet[r].add(board[r][c])
                gridSet[(r // 3, c // 3)].add(board[r][c])
        return True









