# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def xor(p,q):
            return bool(p) ^ bool(q)
        def same(p,q):
            if xor(not p, not q):
                return False
            elif not p and not q:
                return True
            elif p.val != q.val:
                return False
            else:
                return same(p.left, q.left) and same(p.right, q.right)
        return same(p,q)

