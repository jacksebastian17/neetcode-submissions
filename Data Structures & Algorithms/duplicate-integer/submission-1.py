class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenNums = []
        for n in nums:
            if n not in seenNums:
                seenNums.append(n)
            else:
                return True
        return False