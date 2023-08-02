class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()
        def dfs(i, r, c):
            if i >= len(word):
                return True
            elif r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != word[i] or (r, c) in path:
                return False
            else:
                path.add((r, c))
                isValid = (dfs(i + 1, r + 1, c) or
                dfs(i + 1, r - 1, c) or
                dfs(i + 1, r, c + 1) or
                dfs(i + 1, r, c - 1))
                path.remove((r, c))
                return isValid
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(0, r, c): return True
        
        return False
    