# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.calculateDepth(root, 0)
    def calculateDepth(self, node: Optional[TreeNode], depth: int) -> int:
        if node is None:
            return depth
        left_depth = self.calculateDepth(node.left, depth + 1)
        right_depth = self.calculateDepth(node.right, depth + 1)
        return max(left_depth, right_depth)