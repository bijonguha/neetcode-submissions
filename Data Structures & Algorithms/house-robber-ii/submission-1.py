class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        if nums == []:
            return 0
        
        if n==1:
            return nums[0]
        elif n==2:
            return max(nums[0], nums[1])
        elif n==3:
            return max(nums)

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[:2])
        dp[2] = max(nums[:3])

        i = 3

        while i<n:
            
            n_copy = nums.copy()
            dp[i] = max(nums[i]+self.rob_easy(n_copy[1:i-1]),
                        self.rob_easy(n_copy[:i]))

            i+=1

        return dp[n-1]

    def rob_easy(self, nums: List[int]) -> int:

        n = len(nums)
        if nums==[]:
            return 0
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0], nums[1])
        if n==3:
            return max(nums[0]+nums[2], nums[1])
        
        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = max(nums[0]+nums[2], nums[1])

        i = 3
        while i<n:
            dp[i] = max(nums[i]+dp[i-2], dp[i-1],nums[i]+dp[i-3])
            i+=1
            

        return dp[n-1]