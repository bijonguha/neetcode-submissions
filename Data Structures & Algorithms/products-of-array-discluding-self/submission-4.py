class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pref = [1]*len(nums)
        suff = [1]*len(nums)

        for i in range(1,len(nums)):
            pref[i] = nums[i-1] * pref[i-1]
            suff[len(nums)-1-i] = nums[len(nums)-i] * suff[len(nums)-i]

        return [pref[i] * suff[i] for i in range(len(nums))]