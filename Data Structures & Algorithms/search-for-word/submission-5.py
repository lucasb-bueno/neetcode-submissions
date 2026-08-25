class Solution:
    """
    notes:
    - return true if given word is in board
    - not reusing same cell (visited set)
    - horizontal or vertical [[1, 0], [0, 1], [0, -1], [-1, 0]]
    - lowercase and uppercase english letters (transform to lowercase)

    algorithm:
    - mark visited cells
    - bfs(r, c, index) -> index of the letter we are searching for 
        - in CAT, index starts at 0, meaning the letter "C"
    - store the curr index and keep incrementing if we find the next letter
    - visited should be cleaned if word is not found after a bfs iteration
    - if index == len(word), stop and return true

    """

    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        visited = set()

        def dfs(r, c, index):
            if (index == len(word)):
                return True

            if not (0 <= r < ROWS and 0 <= c < COLS) or (r, c) in visited or board[r][c] != word[index]:
                return False
            
            visited.add((r, c))
                
            
            res = dfs(r + 1, c, index + 1) or dfs(r - 1, c, index + 1) or dfs(r, c + 1, index + 1) or dfs(r, c - 1, index + 1)
            
            visited.remove((r, c))
            return res  
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        return False


        
        
        