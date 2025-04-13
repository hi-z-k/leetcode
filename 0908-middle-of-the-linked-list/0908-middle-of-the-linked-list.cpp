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
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        if (head == nullptr) return nullptr;
        ListNode* fast = head;
        ListNode* prev = head;
        while(true){
            prev = head;
            head = head->next;
            if(fast!=nullptr && fast->next!=nullptr) {
                fast = fast->next->next;
            }
            else break; 
        }
        return prev;
    }
};