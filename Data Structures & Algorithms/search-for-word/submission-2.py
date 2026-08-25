class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        notes:
        - return true if word is present on board, false otherwise
        - horizontally or vertically neighbor cells [[1, 0], [-1, 0], [0, 1, [0, -1]]]
        - maybe not be used twice (check if visited)
        - lowercase and uppercase english letters (edge case)

        algorithm:
        - iterate throught board and check if first letter of word is present

        """

        ROWS, COLS = len(board), len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c, visited, index):
            if index == len(word) - 1:
                return True
            
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited and board[nr][nc] == word[index + 1]:
                    if dfs(nr, nc, visited, index + 1):
                        return True
            
            visited.remove((r, c))
            return False


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r, c, set(), 0):
                        return True
        return False