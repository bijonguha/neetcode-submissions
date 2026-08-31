class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]
        
        def backtrack(i, j, ind):
            if ind == len(word):
                return True
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if visited[i][j] or board[i][j] != word[ind]:
                return False
            
            visited[i][j] = True
            
            # Explore neighbors: up, down, left, right
            found = (backtrack(i + 1, j, ind + 1) or
                    backtrack(i - 1, j, ind + 1) or
                    backtrack(i, j + 1, ind + 1) or
                    backtrack(i, j - 1, ind + 1))
            
            visited[i][j] = False
            return found
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if backtrack(i, j, 0):
                        return True
        return False
