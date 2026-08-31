"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

      if not node:
          return None

      visited = {}

      def dfs(current):
          if current in visited:
              return visited[current]

          # Clone the node
          clone = Node(current.val)
          visited[current] = clone

          # Clone neighbors recursively
          for neighbor in current.neighbors:
              clone.neighbors.append(dfs(neighbor))

          return clone

      return dfs(node)     
        
        
        