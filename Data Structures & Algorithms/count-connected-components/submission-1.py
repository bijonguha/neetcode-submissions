class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

      adjl = {i:[] for i in range(n)}

      for n1,n2 in edges:
        adjl[n1].append(n2)
        adjl[n2].append(n1)
      visited = set()

      def dfs(i):
        
        if i in visited:
          return
        
        visited.add(i)

        for j in adjl[i]:
          if j not in visited:
            dfs(j)

      count = 0
      for k,v in adjl.items():
        if k not in visited:
          dfs(k)
          count+=1

      return count
