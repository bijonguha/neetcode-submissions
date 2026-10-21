from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        ct = Counter(nums)

        arr = [[] for i in range(len(nums)+1)]


        for key,freq in ct.items():
            arr[freq].append(key)

        res = []

        for freq in range(len(arr)-1,0,-1):
            for n in arr[freq]:
                res.append(n)

                if len(res) == k:
                    return res
