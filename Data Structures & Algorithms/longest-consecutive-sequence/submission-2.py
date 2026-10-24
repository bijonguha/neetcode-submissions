class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        nums.sort()

        a = [0]*len(nums)

        for i in range(1,len(nums)):
            a[i-1]=nums[i]-nums[i-1]
        
        from collections import defaultdict
        d = defaultdict(list)

        d[0]=[]
        j=1
        i=0
        while i<len(a):
            if a[i] == 1:
                d[j].append(a[i])
            if a[i] > 1:
                j+=1
            i+=1
        
        return max([len(l) for l in list(d.values())])+1
            