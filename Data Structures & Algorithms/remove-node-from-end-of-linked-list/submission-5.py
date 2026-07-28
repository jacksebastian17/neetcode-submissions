# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = 0
        curr = head
        while curr is not None:
            sz += 1
            curr = curr.next
        if sz == n:
            return head.next
        curr = head
        i = 1
        while curr is not None:
            if sz - i == n:
                print(curr.val)
                nextNode = curr.next.next
                curr.next = nextNode
                return head
            i += 1
            curr = curr.next