class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict

        gr = defaultdict(int)

        for n in nums:
            gr[n] += 1
        
        res = sorted(gr.items(), key = lambda k : k[1], reverse=True)

        return [r[0] for r in res[:k]]