class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
            
        max_seq = 1
        cur_seq = 1

        nums = sorted(nums)

        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] == 1:
                cur_seq += 1
            
            elif nums[i] - nums[i-1] == 0:
                continue

            else:
                cur_seq = 1
            
            if cur_seq > max_seq:
                max_seq = cur_seq

        return max_seq