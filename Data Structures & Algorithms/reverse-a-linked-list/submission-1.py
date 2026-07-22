# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        prev = None
        curr = head
        while curr is not None:
            nextNode = curr.next
            # prev = None, curr = 0, curr.next = 1, nextNode = 1
            curr.next = prev 
            # prev = None, curr = 0, curr.next = None, nextNode = 1
            prev = curr
            # prev = 0, curr = 0, curr.next = None, nextNode = 1
            curr = nextNode
            # prev = 0, curr = 1, curr.next = None, nextNode = 1
        return prev