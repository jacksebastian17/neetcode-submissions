class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            res = target - nums[i]
            if res in seen:
                return [seen[res], i]
            seen[nums[i]] = i


"""
nums[i] + nums[j] == target
nums[j] = target - nums[i]

seen = {3, 0}
res = 7 - 4 = 3
3 is in seen, so return i and seen[res]
"""