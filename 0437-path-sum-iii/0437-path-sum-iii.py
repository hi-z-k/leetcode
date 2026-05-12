class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def count(node, current_target):
            if not node:
                return 0
            c = 0 
            if node.val == current_target:
                c += 1
            c += count(node.left, current_target - node.val)
            c += count(node.right, current_target - node.val)
            return c

        def dfs(node):
            if not node:
                return 0
            
            return count(node, targetSum) + dfs(node.left) + dfs(node.right)

        return dfs(root)