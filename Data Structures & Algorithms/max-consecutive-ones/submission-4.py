class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = 0
        currOnes = 0
        for n in nums:
            if n == 1:
                currOnes += 1
            else:
                if currOnes >= maxOnes:
                    maxOnes = currOnes
                currOnes = 0
        
        
        if currOnes >= maxOnes:
            return currOnes
        return maxOnes