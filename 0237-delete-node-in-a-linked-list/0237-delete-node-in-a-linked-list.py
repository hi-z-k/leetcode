# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 1->2->3->4
        prev = node
        curr = node.next
        lastNode = None
        while curr:
            prev.val = curr.val
            if not curr.next:
                lastNode = prev
            prev = curr
            curr = curr.next
        lastNode.next = None