# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        """
        approach 1: recursive, carry = recursion(node)
        approach 2: keep a last_non9 pointer, make this 1, rest all on right 0
        if this last_non9 is dummy, then all 9's -> need to add 1 to front
        """
        # given non-neg int i.e., LL
        dummy = ListNode(0)
        dummy.next = head

        last_non9 = dummy
        curr = head
        while curr:
            if curr.val < 9:
                last_non9 = curr
            curr = curr.next
        
        last_non9.val += 1

        curr = last_non9.next
        while curr:
            curr.val = 0
            curr = curr.next
        
        if last_non9.next == head:
            dummy.val = 1
            return dummy
        
        return dummy.next
        




