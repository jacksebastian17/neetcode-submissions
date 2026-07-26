class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        sorted_counts = sorted(counts, key=counts.get, reverse=True)
        return sorted_counts[0]