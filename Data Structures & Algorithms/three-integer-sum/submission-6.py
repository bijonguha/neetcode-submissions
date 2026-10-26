class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        print(nums)
        res = []
        i = 0

        while i < len(nums)-2:
            if nums[i] > 0:
                break
                
            j = i+1
            k = len(nums)-1

            if i>0 and nums[i] == nums[i-1]:
                i += 1
                continue

            while j<k:
                if nums[j] == nums[j-1] and j-1 != i:
                    j += 1
                    continue

                if nums[i]+nums[j]+nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])

                if nums[i]+nums[j]+nums[k] > 0:
                    k -= 1
                else:
                    j += 1
            
            i += 1

        return res