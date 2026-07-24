# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find mid point of linked list
        if head is None or head.next is None:
            return None
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        second_half = slow.next
        slow.next = None
        
        # reverse second_half linked list
        prev = None
        curr = second_half
        while curr is not None:
            tempNext = curr.next
            curr.next = prev
            prev = curr
            curr = tempNext
        
        # prev is now head of reversed second_half
        # make first_half.next be second_half
        # [2,4,6] [12,10,8]
        # [2,12,4,10,6,8]
        curr1 = head
        curr2 = prev
        while curr2 is not None:
            tempNext1 = curr1.next # 4
            tempNext2 = curr2.next # 10
            curr1.next = curr2 # 2->12
            curr2.next = tempNext1 #12->4
            curr1 = tempNext1
            curr2 = tempNext2

        
        