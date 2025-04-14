/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
#include <map>
class Solution {
public:
    bool hasCycle(ListNode* head) {
        map<ListNode*,int> address;
        while(true){
            if(head==nullptr){
                return false;
            }
            if(!address.count(head)){
                address[head] = 1;
                head = head->next;
            }
            else{
                return true;
            }
        }
        return true;
    }
};