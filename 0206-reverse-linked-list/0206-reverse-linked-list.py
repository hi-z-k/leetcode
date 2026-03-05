# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        new_node = head
        nums = []
        while node:
            nums.append(node.val)
            node = node.next
        for num in nums[::-1]:
            new_node.val = num
            new_node = new_node.next
        return head
