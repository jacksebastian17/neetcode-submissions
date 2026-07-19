import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = s.lower()
        s3 = re.sub(r'[^a-zA-Z0-9]', '', s2)
        new_s = s3.replace(" ", "")
        i = 0
        j = len(new_s)-1
        while (i < len(new_s) // 2):
            if (new_s[i] != new_s[j]):
                return False
            i += 1
            j -= 1
        return True