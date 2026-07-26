# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Find index to remove at
        curr = head
        length = 0
        while curr is not None:
            curr = curr.next
            length += 1
        indexToRemove = length - n

        # Remove head
        if indexToRemove == 0:
            return head.next

        # Remove nth node
        i = 0
        curr = head
        while curr is not None:
            if i + 1 == indexToRemove:
                curr.next = curr.next.next
                return head
            curr = curr.next
            i += 1
        return head
        