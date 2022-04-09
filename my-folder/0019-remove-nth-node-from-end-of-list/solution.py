# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length_ll = 0
        curr = head
        while(curr != None):
            curr = curr.next
            length_ll += 1
        
        idx_to_remove = length_ll - n
        
        if idx_to_remove == 0:
            head = head.next
            return head
        
        prev = head
        curr = head
        for i in range(idx_to_remove):
            prev = curr
            curr = curr.next
        
        prev.next = curr.next
        
        return head
        
        
