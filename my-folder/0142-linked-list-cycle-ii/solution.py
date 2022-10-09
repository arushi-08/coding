# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         a + c = b
#          before loop + loop = between loop
        slow_ptr = head
        prev_slow = None
        fast_ptr = head
        while (slow_ptr != fast_ptr or not prev_slow) and fast_ptr and fast_ptr.next:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
            prev_slow = ListNode(0)
        
        if not fast_ptr or not fast_ptr.next or slow_ptr != fast_ptr:
            return 
        
        slow_ptr = head
        while slow_ptr != fast_ptr:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next
        return slow_ptr
