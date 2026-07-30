class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        n = columnNumber
        while n > 0:
            n -= 1          # shift to 0-index
            digit = chr(ord('A') + n % 26)
            result.append(digit)
            n //= 26
        return ''.join(reversed(result))