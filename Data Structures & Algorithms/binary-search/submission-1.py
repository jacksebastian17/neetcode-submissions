class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and nums[0] == target:
            return 0
        
        left, right = 0, len(nums) - 1 # left=0, right=5
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
            

"""
[-1,0,2,4,6,8]
  l   m     r
m = 2 < 4, move l to m + 1
[-1,0,2,4,6,8]
        l m r
m = 6 > 4, move r to m
[-1,0,2,4,6,8]
        lr
"""