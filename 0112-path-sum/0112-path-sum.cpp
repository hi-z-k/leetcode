/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
bool hasPathSum(TreeNode* root, int targetSum) {
    if (root) {
        int currentVal =  targetSum - root->val;
        if (!root->left && !root->right) {
            if (currentVal == 0) return true;
            else if (currentVal < 0) return false;
        }
        return hasPathSum(root->left, currentVal) || hasPathSum(root->right, currentVal);
    }
    return false;
}
};