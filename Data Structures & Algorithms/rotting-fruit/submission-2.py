class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

      ROWS, COLS = len(grid), len(grid[0])

      visit = []
      queue = deque()

      for i in range(ROWS):
        for j in range(COLS):
          if grid[i][j]==2:
            queue.append((i,j))

      count = 0
      while queue and True in [1 in i for i in grid]:
        count+=1
        for i in range(len(queue)):
          r,c = queue.popleft()
          nbrs = [(1,0),(-1,0),(0,1),(0,-1)]

          for dr,dc in nbrs:
            nr,nc = r+dr, c+dc

            if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
              grid[nr][nc] = 2
              queue.append((nr, nc))
      
      if True in [1 in i for i in grid]:
        return -1

      return count