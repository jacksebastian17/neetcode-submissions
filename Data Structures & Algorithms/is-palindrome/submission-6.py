class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = "".join(c.lower() for c in s if c.isalnum())
        # stripped = wasitacaroracatisaw len=19 // 2 = 9.5 = 9
        i = 0
        j = len(stripped) - 1
        while i < j:
            if stripped[i] != stripped[j]:
                return False
            i += 1
            j -= 1
        return True
