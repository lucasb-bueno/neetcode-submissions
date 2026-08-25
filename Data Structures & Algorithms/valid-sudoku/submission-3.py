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

        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True









