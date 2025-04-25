/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
 #include <vector>
class Solution {
public:
    bool palindrome(vector<int> nums){
    vector<int> inverse;
    for(int i=nums.size()-1;i>=0;i--){
        inverse.push_back(nums.at(i));
    }
    return (nums == inverse);
}
    bool isPalindrome(ListNode* head) {
        vector<int> values;
        while(head->next!=nullptr){
            values.push_back(head->val);
            head = head->next;
        }
        values.push_back(head->val);
        int i=0;
        int j=values.size()-1;
        return palindrome(values);
    }
};

