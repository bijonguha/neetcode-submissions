class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = 1
        j=0
        for i in nums:
            if i != 0:
                res = res * i
            else:
                j = j+1
        if j>1:
            return [0]*len(nums)
        elif j==1:
            return [0 if i !=0 else res for i in nums]
        else:
            return [int(res/i) for i in nums]