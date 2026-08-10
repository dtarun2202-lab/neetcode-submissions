class Solution:
    def lengthOfLongestSubstring(self, s):
        seen = {}    # char → its latest index
        left = 0
        best = 0

        for right in range(len(s)):
            char = s[right]

            # if char seen AND it's inside current window
            if char in seen and seen[char] >= left:
                left = seen[char] + 1   # shrink window from left

            seen[char] = right          # update latest index
            best = max(best, right - left + 1)

        return best