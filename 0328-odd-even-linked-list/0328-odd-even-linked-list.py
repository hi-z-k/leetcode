class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        node = head
        nums = [[],[]]
        while node:
            even, odd = nums
            num = node.val
            if count % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
            count += 1
            node = node.next
        even, odd = nums
        even.extend(odd)
        nums = even
        new_node = head
        for num in nums:
            new_node.val = num
            new_node = new_node.next
        return head