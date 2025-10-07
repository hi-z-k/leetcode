class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rabbit, turtle = head, head
        haveCycle = False

        while rabbit and rabbit.next:
            rabbit = rabbit.next.next
            turtle = turtle.next
            if turtle == rabbit:
                haveCycle = True
                break

        if not haveCycle: 
            return None
        
        turtle = head
        while turtle != rabbit:
            rabbit = rabbit.next
            turtle = turtle.next
        return turtle