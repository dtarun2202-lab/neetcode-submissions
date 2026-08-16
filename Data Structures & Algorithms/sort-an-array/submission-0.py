class Solution:
    def sortArray(self, nums):
        # base case → single element already sorted
        if len(nums) <= 1:
            return nums

        # DIVIDE → split in half
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])   # sort left half
        right = self.sortArray(nums[mid:])  # sort right half

        # CONQUER → merge sorted halves
        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = 0    # pointer for left
        j = 0    # pointer for right

        # compare elements from both halves
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])   # left is smaller → take it
                i += 1
            else:
                result.append(right[j])  # right is smaller → take it
                j += 1

        # add remaining elements
        result.extend(left[i:])    # leftover from left
        result.extend(right[j:])   # leftover from right

        return result