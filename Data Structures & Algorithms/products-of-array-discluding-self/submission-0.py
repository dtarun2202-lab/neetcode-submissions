class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        result = [1] * n

        # left pass: result[i] = product of everything left of i
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        # right pass: multiply by product of everything right of i
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result