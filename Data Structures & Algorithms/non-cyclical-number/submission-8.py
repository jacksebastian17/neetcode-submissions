class Solution:
    def isHappy(self, n: int) -> bool:
        slow = self.sumOfDigits(n)
        fast = self.sumOfDigits(self.sumOfDigits(n))

        while slow != 1:
            if slow == fast:
                return False

            slow = self.sumOfDigits(slow)
            fast = self.sumOfDigits(self.sumOfDigits(fast))

        return True

    def sumOfDigits(self, n: int) -> int:
        total = 0

        while n > 0:
            digit = n % 10
            total += digit**2
            n //= 10

        return total
