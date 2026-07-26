class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        seen = set()
        while True:
            result = 0
            while n > 0:
                result += (n % 10)**2
                n //= 10
            print(result)
            if result == 1:
                return True
            if result in seen:
                return False
            n = result
            seen.add(result)