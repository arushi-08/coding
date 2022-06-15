# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return None
        slow = head
        fast = head
        isCycle = False
        while slow and fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                isCycle = True
                break
        
        if not isCycle: return None
        
        check = head
        
        while check and slow:
            if check == slow:
                return check
            check = check.next
            slow = slow.next
        
        return None
        
        
        
        
