class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        # Phase 1: Find where slow and fast collide
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast: # found a cycle
                break

        # Phase 2: Find the START of the cycle
        finder = 0

        while finder != slow:
            finder = nums[finder]
            slow = nums[slow]

        return finder