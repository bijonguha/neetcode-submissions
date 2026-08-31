class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
      ROWS, COLS = len(grid), len(grid[0])
      INF = 2147483647
      queue = deque()
      
      # Enqueue all treasure chests
      for r in range(ROWS):
          for c in range(COLS):
              if grid[r][c] == 0:
                  queue.append((r, c))

      distance = 0
      directions = [(1,0), (-1,0), (0,1), (0,-1)]

      while queue:
          distance += 1
          for _ in range(len(queue)):
              r, c = queue.popleft()
              for dr, dc in directions:
                  nr, nc = r + dr, c + dc
                  # Check boundaries and if unvisited land cell
                  if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == INF:
                      grid[nr][nc] = distance
                      queue.append((nr, nc))