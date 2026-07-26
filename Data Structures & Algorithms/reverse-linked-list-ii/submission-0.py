# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left_prev = dummy
        for _ in range(left - 1):
            left_prev = left_prev.next
        print(left_prev.val)

        prev = None
        curr = left_prev.next
        for _ in range(right - left + 1): # 4 - 2 + 1 = 3
            tempNext = curr.next
            curr.next = prev
            prev = curr
            curr = tempNext
        saved = left_prev.next # 2
        left_prev.next = prev
        saved.next = curr
        return dummy.next


"""
[1,2,3,4,5,6], left = 2, right = 4

                         left               right
dummy ->     1      ->    2       -> 3 ->    4     -> 5 -> 6
          left_prev      curr

                         left                  right
dummy ->     1      ->    2   -> None         3   ->    4     -> 5 -> 6
          left_prev      prev                curr
             ---------------------
             |                   |
dummy ->     1            3   -> 2 -> None     4  -> 5 -> 6
          left_prev      prev                 curr
  
             ------------------------
             |                      |
dummy ->     1            4 -> 3 -> 2 -> None     5   -> 6
          left_prev      prev                    curr
             
 
dummy ->     1      ->     4 -> 3 ->   2     -> None     5   -> 6
          left_prev      prev        saved              curr
"""