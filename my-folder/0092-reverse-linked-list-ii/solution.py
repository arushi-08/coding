# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        # reverse nodes from left to right
        if left == right:
            return head

        prev = ListNode(0)
        og_head = prev
        prev.next = head
        curr = head
        
        i = 1
        while curr and i != left:
            prev = curr
            curr = curr.next
            i += 1
        
        if not curr: return head 
        
        curr_copy = curr
        prev_copy = prev
        
        while curr and i != right:
            temp = curr.next
            curr.next = prev
            # print('curr', curr.val, 'curr.next', curr.next.val)
            prev = curr 
            curr = temp
            i += 1

        # print('curr_copy', curr_copy.val, curr.val)
        if curr and i == right:
            # print('prev_copy', prev_copy.val, curr.val)
            prev_copy.next = curr
            curr_copy.next = curr.next
            curr.next = prev # cycle
            # print('curr_copy', curr_copy.val, curr.next.val)
            # curr_copy.next = curr.next
        
        return og_head.next


