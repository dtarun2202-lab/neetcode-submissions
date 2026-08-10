from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        count = Counter(nums)   # {1:3, 2:2, 3:1}

        # sort by frequency descending, take first k
        return [num for num, freq in count.most_common(k)]