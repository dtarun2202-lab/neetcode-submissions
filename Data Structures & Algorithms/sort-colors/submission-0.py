class Solution:
    def sortColors(self, nums):
        low = 0              # boundary for 0s
        mid = 0              # current element being examined
        high = len(nums) - 1 # boundary for 2s

        while mid <= high:
            if nums[mid] == 0:
                # swap with low, move both forward
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                # already in right place, just move mid
                mid += 1

            else:
                # nums[mid] == 2
                # swap with high, move high back (NOT mid!)
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1