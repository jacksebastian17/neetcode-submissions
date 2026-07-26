class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while left < right:
            num = (left + right) // 2
            if guess(num) == 1:
                left = num + 1
            elif guess(num) == -1:
                right = num - 1
            else:
                return num
        return left
        


            