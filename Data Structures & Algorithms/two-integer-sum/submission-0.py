class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, x in enumerate(nums): # (0,3) -> (1,4) -> (2,5)
            complement = target - x
            if complement in seen:
                return [seen[complement], i]
            seen[x] = i



# seen = {}
# i=0, x=3
# complement = 7 - x = 7 - 3 = 4
# is 4 in seen? no -> seen = {3: 0}
# i=1, x=4
# complement = 7 - x = 7 - 4 = 3
# is 3 in seen? yes -> return [seen[complement], i]