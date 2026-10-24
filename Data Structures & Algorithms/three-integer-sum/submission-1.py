class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        i = 0
        while i <= len(nums)-3:
            j = i+1
            k = len(nums)-1

            target = 0-nums[i]

            while j<k:

                if nums[j]+nums[k] == target:
                    if [nums[i], nums[j], nums[k]] not in res:
                        res.append([nums[i], nums[j], nums[k]])
                
                if nums[j]+nums[k] < target:
                    j += 1
                else:
                    k -= 1
            
            i += 1
        
        return res