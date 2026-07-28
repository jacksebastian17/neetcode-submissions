# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find midpoint of list
        if head is None or head.next is None:
            return None 
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        # break off the midpoint.next so we have list1 and list2
        list2 = slow.next
        slow.next = None
        list1 = head
        # reverse list2
        prev = None
        curr = list2
        while curr is not None:
            tempNext = curr.next
            curr.next = prev
            prev = curr
            curr = tempNext
        list2 = prev
        # link list1.next to be list2 until list fully connected
        # list1 = [2,4,6]
        # list2 = [10,8]
        while list1 is not None and list2 is not None:
            list1next = list1.next
            list2next = list2.next
            list1.next = list2
            list2.next = list1next
            list1 = list1next
            list2 = list2next
        