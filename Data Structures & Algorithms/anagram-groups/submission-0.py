from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        groups = defaultdict(list)  # key: sorted string, value: list of anagrams

        for word in strs:
            key = "".join(sorted(word))  # sort the word → use as key
            groups[key].append(word)     # add word to its group

        return list(groups.values())