class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        while low <= high:
            med = low + (high - low) // 2
            if nums[med] < target:
                low = med + 1
            elif nums[med] > target:
                high = med - 1
            else:
                return med
        return -1

# [-1,0,2,4,6,8] target=4
#   l   m     h
# [-1,0,2,4,6,8]
#       l m   h
# [1,3] target=3
#  l h
# 