class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # {3: 0}
        for i in range(len(nums)): # 1
            complement = target - nums[i] # 7 - nums[1] = 7 - 4 = 3
            if complement in seen: # is 3 in seen? yes
                return [seen.get(complement), i] # [seen.get(nums[1]), 1] = [see]
            seen[nums[i]] = i