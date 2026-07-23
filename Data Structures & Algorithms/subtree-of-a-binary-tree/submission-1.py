# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.isMatch(root, subRoot) == True:
            return True
        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None:
            return False
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isMatch(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return (self.isMatch(p.left, q.left) and self.isMatch(p.right, q.right))

"""
1. traverse down root tree, and always start at subRoot for other tree
2. eval nodes and return back False when we see 2 nodes values not matching
"""