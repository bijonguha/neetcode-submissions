class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

      m, n = len(grid), len(grid[0])

      marked = [[-1]*n]*m
      count = 0

      def backtrack(i,j,visited):

        if i<0 or j<0 or i>=m or j>=n:
          return

        if visited[i][j] != 0:
          return

        if grid[i][j] != "1":
          return

        visited[i][j] = 1

        backtrack(i+1, j, visited)
        backtrack(i-1, j, visited)
        backtrack(i, j+1, visited)
        backtrack(i, j-1, visited)

        return

      for i in range(m):
        for j in range(n):
          if grid[i][j] == "1" and marked[i][j] == -1:
            visited = [[0 for i in range(n)] for j in range(m)]
            backtrack(i, j, visited)
            count += 1
            marked = [[count if i==1 else j for (i,j) in zip(ll,mm)] for ll,mm in zip(visited,marked)]

      return count 