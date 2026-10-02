class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)

        # Put every valid number in its correct position
        i = 0

        while i < n:
            correct_index = nums[i] - 1

            if (
                1 <= nums[i] <= n
                and nums[i] != nums[correct_index]
            ):
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i += 1

        # Find the first number that isn't in its correct position
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1