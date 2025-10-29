class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        emptyNode = ListNode(0, head)
        start = emptyNode
        for i in range(left - 1):
            start = start.next
        stack = []
        current = start.next 
        for i in range(left-1, right):
            stack.append(current)
            current = current.next
        one_after = current
        while stack:
            start.next = stack.pop()
            start = start.next
        start.next = one_after
        return emptyNode.next