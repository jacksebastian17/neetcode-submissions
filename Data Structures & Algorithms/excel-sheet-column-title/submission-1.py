class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        n = columnNumber
        while n > 0:
            n -= 1                          # shift to 0-index
            digit = n % 26                  # 0...25
            letter = chr(ord('A') + digit) # letter = char()
            result.append(letter)
            n //= 26
        return ''.join(reversed(result))