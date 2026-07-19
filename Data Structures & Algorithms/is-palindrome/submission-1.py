import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = s.lower()
        s3 = re.sub(r'[^a-zA-Z0-9]', '', s2)
        i = 0
        j = len(s3)-1
        while (i < len(s3) // 2):
            if (s3[i] != s3[j]):
                return False
            i += 1
            j -= 1
        return True