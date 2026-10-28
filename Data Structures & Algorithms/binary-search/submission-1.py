class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def helper(l: int, r: int) -> int:
            if l > r:                    # base case: empty range → not found
                return -1

            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                return helper(m + 1, r)  # search the right half
            else:
                return helper(l, m - 1)  # search the left half

        return helper(0, len(nums) - 1)