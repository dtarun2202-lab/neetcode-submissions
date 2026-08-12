from collections import defaultdict

class Solution:
    def subarraySum(self, nums, k):
        count = 0
        prefix = 0
        seen = defaultdict(int)
        seen[0] = 1              # empty subarray has sum 0

        for num in nums:
            prefix += num
            count += seen[prefix - k]   # how many times (prefix-k) seen before
            seen[prefix] += 1

        return count