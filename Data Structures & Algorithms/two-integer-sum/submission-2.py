from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = defaultdict(list)

        for i,n in enumerate(nums):
            d[n].append(i)

        for i,j in d.items():
            n = target - i
            
            if (n == i) and (len(d[i])>1):
                return [d[i][0],d[i][1]]

            if (n != i) and n in d:
                return [j[0], d[n][0]]
            
