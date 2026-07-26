# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find midpoint
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None

        # head1 = 2 -> 4 -> 6 -> None 
        # head2 = 8 -> 10 -> 12 -> None
        # reverse 2nd list
        prev = None
        curr = head2
        while curr is not None:
            tempNext = curr.next
            curr.next = prev
            prev = curr
            curr = tempNext
        head2 = prev

        # linkage
        # head  = 2 -> 4 -> 6 -> None 
        # head2 = 12 -> 10 -> 8 -> None
        while head2 is not None:
            next1 = head.next # 4
            next2 = head2.next # 10

            head.next = head2
            head2.next = next1

            head = next1
            head2 = next2
