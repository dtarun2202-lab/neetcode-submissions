class Solution:

    def encode(self, strs):
        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s   # "5#hello"

        return result

    def decode(self, s):
        result = []
        i = 0

        while i < len(s):
            # find the '#' separator
            j = i
            while s[j] != "#":
                j += 1

            # extract length
            length = int(s[i:j])

            # extract word
            word = s[j + 1 : j + 1 + length]
            result.append(word)

            # move i to start of next encoded word
            i = j + 1 + length

        return result