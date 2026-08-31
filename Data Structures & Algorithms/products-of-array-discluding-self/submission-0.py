class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        dnums = [nums.copy() for i in nums]

        for i in range(len(nums)):
            for j in range(len(nums)):

                if i == j:
                    dnums[i][j] = 1
                    break

        import math
        dnums = [math.prod(i) for i in dnums]

        return dnums
        