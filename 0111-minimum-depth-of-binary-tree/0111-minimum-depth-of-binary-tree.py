# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        minDepth = float("inf")
        if not root:
            return 0
        def eachdepth(node):
            nonlocal depth
            nonlocal minDepth
            if not node:
                return 
            depth += 1
            if not node.left and not node.right:
                minDepth = min(minDepth,depth)
            else:
                eachdepth(node.left)
                eachdepth(node.right)
            depth -= 1
        eachdepth(root)
        return minDepth