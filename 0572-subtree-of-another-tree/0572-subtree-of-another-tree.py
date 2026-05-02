# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSub(root):
            if not root:
                return False
            leftSubRoot = root.left
            rightSubRoot = root.right
            if not same(root,subRoot)  and not same(leftSubRoot,subRoot) and not same(rightSubRoot,subRoot):
                return isSub(leftSubRoot) or isSub(rightSubRoot)
            return True
        return isSub(root)