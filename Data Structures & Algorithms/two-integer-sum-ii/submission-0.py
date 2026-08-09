class Solution:
    def twoSum(self, numbers, target):
        left = 0                    # start pointer
        right = len(numbers) - 1   # end pointer

        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left + 1, right + 1]  # +1 because 1-indexed
            elif total < target:
                left += 1    # need bigger sum → move left right
            else:
                right -= 1   # need smaller sum → move right left