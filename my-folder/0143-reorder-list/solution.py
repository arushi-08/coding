# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        last = head
        curr = head
       
        while curr.next:
            last = curr.next
            prevlast = None
            
            while last.next:
                prevlast = last
                last = last.next

            if curr.next == last:
                break
            self.reorder_curr_n_last_nodes(curr, last, prevlast)
            curr = last.next
    
    def reorder_curr_n_last_nodes(self, curr, last, prevlast):
                         # e.g. 1->2->3->4->None 
        temp = curr.next # 2
        if last.next:
            prevlast.next = last.next
        else:
            prevlast.next = None
        curr.next = last # 1->4
        last.next = temp # 4->2
