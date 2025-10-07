# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# approach => first let's detect if there is a cycle to begin with => using FLoyd's Algorithm
    # => having a fast pointer and a slow pointer, and the only chance they become equal is if there is a cycle
    # => If we detect a cycle => reset slow pointer to the head and slow down the rabbit's speed from 2 to 1, when they meet will be
    # the head of the cycle and also keep a count of this process
    # time complexity => O(m+nC) where m is the non cyclic part and nC is a multiple of the cycle part => Boiling down to O(n)
    # space complexity => O(1) we essentially need to maintain few variable that points to nodes

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