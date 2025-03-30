# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        # head of LL & value x
        # partition it such that all nodes < x come before nodes > x

        # store all elements > x, if any elem < x found save beg node and iterate till <x no more , swap them?

        curr = head
        prev = ListNode(-1)
        prev.next = curr
        lt_x_head = ListNode(-1)
        lt_x_curr = lt_x_head
        gt_x_head = ListNode(-1)
        gt_x_curr = gt_x_head
        while curr:
            if curr.val < x:
                prev.next = None
                lt_x_curr.next = curr
                lt_x_curr = curr
            else:
                prev.next = None
                gt_x_curr.next = curr
                gt_x_curr = curr
            
            prev = curr
            curr = curr.next
        
        lt_x_curr.next = gt_x_head.next
        new_head = lt_x_head.next

        return new_head


