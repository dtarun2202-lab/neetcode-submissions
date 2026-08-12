from collections import Counter

class Solution:
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        need = Counter(s1)          # frequency of s1
        window = Counter(s2[:len(s1)])  # first window of s2

        if need == window:
            return True

        for i in range(len(s1), len(s2)):
            # add new char on right
            window[s2[i]] += 1

            # remove old char on left
            left_char = s2[i - len(s1)]
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]   # clean up zeros

            if window == need:
                return True

        return False