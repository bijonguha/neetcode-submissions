class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(nums)                 # copy, don't mutate
        best = cur = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:        # duplicate: skip
                continue
            if nums[i] == nums[i-1] + 1:    # extends the run
                cur += 1
            else:                           # gap: start over
                cur = 1
            best = max(best, cur)
        return best