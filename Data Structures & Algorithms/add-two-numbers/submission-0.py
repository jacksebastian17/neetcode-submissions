# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        result = dummy
        carry = 0
        while l1 is not None or l2 is not None:
            if l1 is None:
                l1 = ListNode(0)
            if l2 is None:
                l2 = ListNode(0)
            summation = ListNode((l1.val + l2.val + carry) % 10)
            print(summation.val)
            carry = (l1.val + l2.val + carry) // 10
            print("carry:", carry)
            result.next = summation
            result = result.next
            l1 = l1.next
            l2 = l2.next
        if carry:
            start = ListNode(1)
            result.next = ListNode(1)
        return dummy.next

"""
l1     = [8,9,9,5,5]
l2     = [4,5,6]
result = [2,5,6,6,5]

  111
 55998
+  654
------
 56652
"""