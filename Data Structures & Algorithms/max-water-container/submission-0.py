class Solution:
    def maxArea(self, heights: List[int]) -> int:
    
      l = 0
      r = len(heights) - 1

      maxw = 0

      while l<r:
        
        h = min(heights[l], heights[r])
        w = r-l

        w = h * w

        if w > maxw:
          maxw = w

        if heights[l] > heights[r]:
          r-=1
        else:
          l+=1
      
      return maxw