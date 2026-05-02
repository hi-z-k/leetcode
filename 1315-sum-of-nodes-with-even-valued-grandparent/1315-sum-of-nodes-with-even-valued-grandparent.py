# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        chain = []
        evenSum = 0
        def sumGrand(node):
            nonlocal evenSum
            if not node:
                return 
            chain.append(node.val)
            if len(chain) > 2 and chain[-3] % 2 == 0:
                evenSum += node.val
            sumGrand(node.left)
            sumGrand(node.right)
            chain.pop()
        sumGrand(root)
        return evenSum
        