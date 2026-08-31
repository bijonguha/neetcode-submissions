## Optimized solution

class Solution:
    def solve(self, board: List[List[str]]) -> None:

      m, n = len(board), len(board[0])
      marked = [[False]*n for _ in range(m)]
      region_cells = []

      def dfs(i, j):
          if i < 0 or j < 0 or i >= m or j >= n:
              return True

          if marked[i][j] or board[i][j] == "X":
              return False

          marked[i][j] = True
          region_cells.append((i,j))
        
          ri = dfs(i+1,j)
          le = dfs(i-1,j)
          up = dfs(i,j+1)
          do = dfs(i,j-1)

          return up or do or le or ri
        
      for i in range(m):
          for j in range(n):
              if board[i][j] == "O" and not marked[i][j]:
                  region_cells.clear()
                  if not dfs(i, j):
                    for x,y in region_cells:
                      board[x][y]="X"

      return
