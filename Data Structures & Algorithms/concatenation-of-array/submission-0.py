class Solution:
    def getConcatenation(self, nums):
        ans = []

        for i in range(2):         # run twice
            for num in nums:       # add all nums each time
                ans.append(num)

        return ans