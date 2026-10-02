class Solution:
    def characterReplacement(self, s, k):
        count = {}

        left = 0
        max_freq = 0
        best = 0

        for right in range(len(s)):
            char = s[right]

            count[char] = count.get(char, 0) + 1

            max_freq = max(max_freq, count[char])

            window_length = right - left + 1
            replacements = window_length - max_freq

            while replacements > k:
                count[s[left]] -= 1
                left += 1

                window_length = right - left + 1
                replacements = window_length - max_freq

            best = max(best, right - left + 1)

        return best