# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return None 
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        list2 = slow.next
        slow.next = None
        list1 = head

        prev = None
        curr = list2
        while curr is not None:
            tempNext = curr.next
            curr.next = prev
            prev = curr
            curr = tempNext
        list2 = prev

        while list1 is not None and list2 is not None:
            n1 = list1.next
            n2 = list2.next
            list1.next = list2
            list2.next = n1
            list1 = n1
            list2 = n2
        