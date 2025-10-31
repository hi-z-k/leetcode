# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    @staticmethod
    def reverse(head: Optional[ListNode]) -> None:
        stack = ListNode()
        temp = head
        while temp:
            nextNode = temp.next
            temp.next = stack.next 
            stack.next = temp
            temp = nextNode
        return stack.next
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = Solution.reverse(head)
        monotonic = stack
        while monotonic and monotonic.next:
            nextN = monotonic.next
            if nextN.val<monotonic.val:
                monotonic.next = nextN.next
                nextN.next = None
            else:
                monotonic = monotonic.next
        return Solution.reverse(stack)