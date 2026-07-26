# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.findDepth(root)
        return self.diameter
    def findDepth(self, node):
        if node is None:
            return 0
        left_depth = self.findDepth(node.left)
        right_depth = self.findDepth(node.right)
        self.diameter = max(self.diameter, left_depth + right_depth)
        return 1 + max(left_depth, right_depth)