class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums) // 2]  # majority element always sits in middle!