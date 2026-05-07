# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        complement = set()
        isFound = False
        def search(root):
            nonlocal isFound
            if root:
                val = root.val
                if val in complement:
                    isFound = True
                complement.add(k - val)
                search(root.left)
                search(root.right)
        search(root)
        return isFound