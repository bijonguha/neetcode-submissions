class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
      m, n = len(grid), len(grid[0])
      marked = [[0]*n for _ in range(m)]

      def dfs(i, j):
          if i < 0 or j < 0 or i >= m or j >= n:
              return
          if marked[i][j] == 1 or grid[i][j] == 0:
              return

          marked[i][j] = 1

          dfs(i+1, j)
          dfs(i-1, j)
          dfs(i, j+1)
          dfs(i, j-1)

      prev_sum = 0
      max_sum = 0

      for i in range(m):
          for j in range(n):
              if grid[i][j] == 1 and not marked[i][j]:
                  dfs(i, j)
                  cur_sum = sum(sum(row) for row in marked) - prev_sum
                  prev_sum = cur_sum + prev_sum
                  if cur_sum > max_sum:
                    max_sum = cur_sum

      return max_sum
