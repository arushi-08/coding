# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # get start, end ptr k - 1 dist apart
        # reverse them
        if k == 1:
            return head
        start = end = head
        prevstart = ListNode(0)
        prevstart.next = start
        prevstart_og = prevstart
        while end:
            i = 1
            while i < k and end:
                end = end.next
                # print('new end', end.val)
                i += 1
            if i == k and end:
                self.reverse(prevstart, start, end)
                prevstart = start
                end = start.next
                start = start.next
                # print('end', end.val, 'start', start.val)
                i = 0
        return prevstart_og.next

    def reverse(self, prev, start, end):
        
        curr = start
        prev_ptr = prev
        end_next = end.next

        while curr and curr != end_next:
            # print('curr.val', curr.val)
            temp = curr.next
            curr.next = prev_ptr
            prev_ptr = curr
            curr = temp
        
        prev.next = end
        start.next = end_next

        temp = prev.next
        while temp != end_next:
            # print(temp.val)
            temp = temp.next


