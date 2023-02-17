# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1: return list2
        if not list2: return list1
        curr1 = list1
        curr2 = list2
        answer = ListNode(-1)
        prehead = answer

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                prehead.next = curr1
                curr1 = curr1.next
            else:
                prehead.next = curr2
                curr2 = curr2.next
            prehead = prehead.next
        while curr1:
            prehead.next = curr1
            curr1 = curr1.next
            prehead = prehead.next
        while curr2:
            prehead.next = curr2
            curr2 = curr2.next
            prehead = prehead.next
        return answer.next

                
            
