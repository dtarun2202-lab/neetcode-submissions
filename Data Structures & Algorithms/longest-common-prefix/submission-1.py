class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:               # empty array → no prefix
            return ""

        prefix = strs[0]           # take first string as reference

        for string in strs[1:]:    # compare with every other string
            # shrink prefix until it matches start of string
            while not string.startswith(prefix):
                prefix = prefix[:-1]   # chop last character off prefix
                if not prefix:
                    return ""          # nothing left → no common prefix

        return prefix
