class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        currNum = self.sumOfDigits(n)
        if currNum == 1:
            return True
        print("about to go in loop:", currNum)
        seen.add(currNum)
        while currNum != 1:
            currNum = self.sumOfDigits(currNum)
            if currNum in seen:
                return False
            print("currNum:", currNum)
            seen.add(currNum)
        return True

        return True
    def sumOfDigits(self, n: int) -> int:
        digits = []
        while n > 0:
            digit = n % 10  
            n = n // 10
            digits.append(digit)
        return sum(x**2 for x in digits)

