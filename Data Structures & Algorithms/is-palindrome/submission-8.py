class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum(): # skip over non-alphanumeric chars
                left += 1
            while left < right and not s[right].isalnum(): # skip over non-alphanumeric chars
                right -= 1
            if s[left].lower() != s[right].lower(): # convert to lowercase and then evaluate
                return False
            left += 1
            right -= 1
        return True
