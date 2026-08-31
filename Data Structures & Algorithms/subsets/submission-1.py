class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        curset, subset = [], []

        def rec(nums, i, curset, subset):
            
            if i >= len(nums):
                subset.append(curset)
                return
            
            curset.append(nums[i])
            rec(nums, i+1, curset.copy(), subset)

            curset.pop()
            rec(nums, i+1, curset.copy(), subset)
        
        rec(nums, 0, curset, subset)

        return subset