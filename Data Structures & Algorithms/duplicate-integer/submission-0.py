class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        n = list(set(nums))

        if len(nums) > len(n):
            return True

        return False
