# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
  1 -> 2 -> 3 -> 4 -> None
  And you want:
  None <- 1 <- 2 <- 3 <- 4
  i.e. return 4 -> 3 -> 2 -> 1 -> None.
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
