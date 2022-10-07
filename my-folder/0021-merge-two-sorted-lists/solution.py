# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr1 = list1
        curr2 = list2
        ans_head = ListNode()
        ans_curr = ans_head
        while curr1 and curr2:
            if curr1.val > curr2.val:
                ans_curr.next = curr2
                curr2 = curr2.next
            else:
                ans_curr.next = curr1
                curr1 = curr1.next
            ans_curr = ans_curr.next
        
        if curr1:
            ans_curr.next = curr1
        elif curr2:
            ans_curr.next = curr2

        return ans_head.next
                
        
