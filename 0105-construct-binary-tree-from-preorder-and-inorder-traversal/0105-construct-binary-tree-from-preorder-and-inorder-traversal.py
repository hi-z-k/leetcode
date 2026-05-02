# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def tree(preorder,inorder):
            if not preorder:
                return None
            root = preorder[0]
            i = inorder.index(root)
            left = tree(preorder[1:i+1], inorder[:i])
            right = tree(preorder[i+1:], inorder[i+1:])
            return TreeNode(root, left, right)
        return tree(preorder,inorder)