from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)        
        buckets = [[] for _ in range(len(nums)+1)]
        
        for val,freq in count.items():
            buckets[freq].append(val)

        res = []

        for freq in range(len(buckets)-1,0,-1):
            for i in buckets[freq]:
                res.append(i)
            if len(res) == k:
                return res


