# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
#         3 -> 2 -> 0 -> 4 -> -> 2
#           slow = 3, 2, 0
#           fast = 2, 4 ,0
        
        slow = head
        if head == None:
            return False
        fast = head.next
        
        while slow != None and fast != None and fast.next != None:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        
        return False
