from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        d = defaultdict(int)

        for n in nums:
            d[n] += 1        

        return any([i>1 for j,i in d.items()])