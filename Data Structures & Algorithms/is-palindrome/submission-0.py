class Solution:
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1

        while left < right:
            # skip non-alphanumeric from left
            while left < right and not s[left].isalnum():
                left += 1

            # skip non-alphanumeric from right
            while left < right and not s[right].isalnum():
                right -= 1

            # compare characters (case insensitive)
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True