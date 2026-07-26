class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.getNext(n)
        while slow != 1:
            if slow == fast:
                return False
            slow = self.getNext(slow)
            fast = self.getNext(self.getNext(fast))
        return True

    def getNext(self, n: int) -> int:
        result = 0
        while n > 0:
            result += (n % 10) ** 2
            n //= 10
        return result