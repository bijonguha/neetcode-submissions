class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

      minp = min(piles)
      maxp = max(piles)

      min_hrs = len(piles)
      max_hrs = sum(piles)

      if h == min_hrs:
        return maxp
      elif h == max_hrs:
        return maxp

      l = 1
      r = maxp

      def timetaken(li, k):

        hrs=0

        import math

        for i in li:

          hrs = hrs+math.ceil(i/k)

        return hrs
      sols = []

      while l<=r:
        
        mid = (l+r)//2

        mid_hrs = timetaken(piles, mid)

        if mid_hrs > h :
          l = mid+1
        elif mid_hrs <= h:
          r = mid-1
          sols.append(mid)
      
      return min(sols)
