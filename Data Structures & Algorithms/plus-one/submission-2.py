class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        carry = True
        i = len(digits) - 1
        while carry:
            if digits[i] == 0:
                digits.insert(0,1)
                return digits
            if digits[i] != 9:
                carry = False
            digits[i] = (digits[i] + 1) % 10
            i -= 1
        return digits