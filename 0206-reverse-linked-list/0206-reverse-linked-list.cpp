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
    ListNode* reverseList(ListNode* head) {
        ListNode* previous = nullptr;
        ListNode* current = head;
        if(current == nullptr) return nullptr;
        ListNode* next = current->next;
        while (current->next!=nullptr) {
            current->next = previous;
            previous=current;
            current = next;
            next = next->next;
        }
    current->next = previous;
    return current;
    }
};