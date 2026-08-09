from collections import Counter

class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):     # different lengths = never anagram
            return False

        return Counter(s) == Counter(t)