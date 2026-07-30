# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        head = root
        curr = root
        while curr is not None:
            if curr.val > val:
                if curr.left is None:
                    curr.left = TreeNode(val)
                    return head
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = TreeNode(val)
                    return head
                curr = curr.right
        return root
        