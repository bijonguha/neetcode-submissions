class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        
        def backtrack(start, cur, target_left):
            # Base case: found valid combination
            if target_left == 0 and cur.copy() not in result:
                result.append(cur.copy())
                return
            # If overshoot target, stop exploring
            if target_left < 0:
                return
            
            # Explore further numbers starting from "start"
            for i in range(start, len(nums)):
                cur.append(nums[i])                # Choose
                backtrack(i+1, cur.copy(), target_left - nums[i])  # Recurse (allow reuse)
                cur.pop()                        # Backtrack (undo choice)
        
        backtrack(0, [], target)
        return result 