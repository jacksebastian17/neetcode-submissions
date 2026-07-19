import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower()
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', lower)
        i, j = 0, len(cleaned)-1
        while i < j:
            if cleaned[i] != cleaned[j]:
                return False
            i += 1
            j -= 1
        return True