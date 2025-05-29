# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        
        # m, n
        # head

        # head = current node
        # keep first m nodes starting with current node
        # remove next n nodes

        curr = head
        while curr:
            i = 0
            while curr and i < m-1:
                curr = curr.next
                i += 1
            
            if not curr:
                break
            i = 0
            prev = curr
            while curr and i <= n:
                curr = curr.next
                i += 1
            
            prev.next = curr
        
        return head
                

