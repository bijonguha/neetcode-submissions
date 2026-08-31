class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

      nums = sorted(nums)
      res = []

      for i in range(len(nums)-2):

        if i>0 and nums[i] == nums[i-1]:
          continue

        l = i+1
        r = len(nums)-1
        c = 0-nums[i]

        while l<r:
          
          if nums[l]+nums[r] == c:
            res.append([nums[i], nums[l],nums[r]])
            l+=1
            r-=1

            while l<r and nums[l] == nums[l-1]:
              l+=1

            while l<r and nums[r] == nums[r+1]:
              r-=1

          elif nums[l]+nums[r] > c:
            r-=1

          elif nums[l]+nums[r] < c:
            l+=1
        
      return res
