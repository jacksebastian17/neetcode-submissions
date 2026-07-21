# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0
        self.calculateHeight(root)
        return self.maxDiameter

    def calculateHeight(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0

        left_height = self.calculateHeight(node.left)
        right_height = self.calculateHeight(node.right)

        currDiameter = left_height + right_height
        self.maxDiameter = max(
            self.maxDiameter,
            currDiameter
        )

        return 1 + max(left_height, right_height)




"""
go down tree. at every node:
1. calculate height of left and right subtree
2. diameter is the sum of them
3. keep track of largest diameter found
"""