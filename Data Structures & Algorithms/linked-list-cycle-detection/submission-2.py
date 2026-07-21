# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        seen = set()
        curr = head
        while curr.next != None:
            if curr.next in seen:
                return True
            seen.add(curr)
            curr = curr.next
        return False
            