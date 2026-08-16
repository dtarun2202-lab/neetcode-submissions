class Solution:
    def removeElement(self, nums, val):
        left = 0                        # tracks where to place next valid element

        for right in range(len(nums)):  # scan every element
            if nums[right] != val:      # found a valid element?
                nums[left] = nums[right] # place it at left position
                left += 1               # move left forward

        return left                     # left = count of valid elements