# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, 2*interval):
                lists[i] = self.merge2Lists(lists[i], lists[i+interval])
            interval*=2
        return lists[0] if amount else None
    
    def merge2Lists(self, l1, l2):
        head = curr = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        
        return head.next

