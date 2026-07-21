# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        left_height = self.height(root.left, 0)
        right_height = self.height(root.right, 0)
        if left_height == -1 or right_height == -1:
            return False
        if abs(left_height - right_height) > 1:
            return False
        return True
    
    def height(self, node: Optional[TreeNode], depth: int) -> int:
        if node is None:
            return depth
        left_height = self.height(node.left, depth + 1)
        if left_height == -1:
            return -1
        right_height = self.height(node.right, depth + 1)
        if right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height)


"""
at each node in tree:
1. calculate the left and right subtree height
2. calculate if abs(left - right) > 1
"""