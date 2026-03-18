# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.iteration = []
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        dfs = self.inorderTraversal
        iteration = self.iteration
        node = root
        if node:
            dfs(node.left)
            iteration.append(node.val)
            dfs(node.right)
        return iteration