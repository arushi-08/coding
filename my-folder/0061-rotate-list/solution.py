# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head, prev=None, k=-2):
        curr = head
        length = 0
        if k == -1: return prev
        while curr:
            temp = curr.next
            curr.next = prev
            # temp.next = curr
            prev = curr
            curr = temp
            if length == k:
                return prev
            length += 1
        return prev


    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # rotate entire list - 5 4 3 2 1
        # rotate till k-1 - 4 5
        # rotate k till n-1 - 1 2 3
        if not head: return
        curr = head
        node_at_k = None
        node_at_k_1 = None
        n = 0
        while curr:
            curr = curr.next
            n += 1
        k %= n
        
        reversed_head = self.reverse(head)
        curr = reversed_head
        for i in range(k):
            curr = curr.next
        node_at_k = curr

        reversed_first_half = self.reverse(
            reversed_head, None, k - 1
            )
        print('reversed_first_half', reversed_first_half)
        print('node_at_k', node_at_k)
        
        reversed_second_half = self.reverse(node_at_k)
        print('reversed_second_half', reversed_second_half)
        curr = reversed_first_half
        while curr and curr.next:
            curr = curr.next
        if not curr:
            reversed_first_half = reversed_second_half
        else:
            curr.next = reversed_second_half
        return reversed_first_half
