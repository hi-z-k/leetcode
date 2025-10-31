# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        numSet = set(nums)
        temp = head
        while temp and temp.next:
            if temp.next.val in numSet:
                temp.next = temp.next.next
            else:
                temp = temp.next
        if head.val in numSet:
            head = head.next
        return head
        