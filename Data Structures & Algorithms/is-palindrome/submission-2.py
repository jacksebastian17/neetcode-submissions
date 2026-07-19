import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower()
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', lower)
        i = 0
        j = len(cleaned)-1
        while (i < j):
            if (cleaned[i] != cleaned[j]):
                return False
            i += 1
            j -= 1
        return True