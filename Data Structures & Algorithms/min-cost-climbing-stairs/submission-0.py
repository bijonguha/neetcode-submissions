class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        st = n+1
        dp = [0]*st
        dp[0] = 0
        dp[1] = 0
        i=2

        def dp_fn(i):
            
            if i<2:
                return 0 

            while i<=n:
                dp[i] = min(dp[i-1]+cost[i-1] , dp[i-2]+cost[i-2])
                i+=1
            return 
        
        dp_fn(i)
        return dp[n]