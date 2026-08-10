class Solution:
    def longestConsecutive(self, nums):
        seen = set(nums)       # convert to set for O(1) lookup
        best = 0

        for num in seen:
            # only start counting if num is the START of a sequence
            if num - 1 not in seen:
                length = 1

                # keep going while next number exists
                while num + length in seen:
                    length += 1

                best = max(best, length)

        return best