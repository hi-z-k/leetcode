# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def build(array):
            if not array:
                return None
            if len(array) == 1:
                return TreeNode(array[0])
            maximum = max(array)
            i = array.index(maximum)
            root = TreeNode(array[i])
            root.left = build(array[:i])
            root.right = build(array[i+1:])
            return root
        return build(nums)