class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

      d = {}

      for i,n in enumerate(numbers):

        comp = target - n

        if comp in d:

          return [d[comp]+1,i+1]
        
        else:

          d[n] = i        