# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = ListNode(0)
        prev.next = head
        prevcopy = prev
        curr = head

        while curr and curr.next:
            prev.next = curr.next
            curr.next = curr.next.next
            prev.next.next  = curr
            # 0 -> 2 | 1 -> 4
            # 1 -> 3 | 3 -> none
            # 2 -> 1 | 4 -> 3
            # 2 1 3 | 1 4 3
            prev = curr
            curr = curr.next
            # curr = 3
            # prev = 1
        
        return prevcopy.next

