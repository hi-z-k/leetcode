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
    ListNode *detectCycle(ListNode *head) {
        map<ListNode*,int> address;
        int i = 0;
        while(true){
            if(head==nullptr) return nullptr;
            
            if(!address.count(head)){
                address[head] = i++;
                head = head->next;
            }
            else return head;
        }
        //return head;
    }  
};
