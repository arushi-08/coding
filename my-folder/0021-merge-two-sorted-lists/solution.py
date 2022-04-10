# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        
        dummy = ListNode(0)
        curr1 = list1
        curr2 = list2
        currdummy = dummy
        
        while(curr1!=None and curr2!=None):
            if curr1.val <= curr2.val:
                currdummy.next = curr1
                curr1 = curr1.next
            else:
                currdummy.next = curr2
                curr2 = curr2.next
            
            currdummy = currdummy.next
        
        while curr1!=None:
            currdummy.next = curr1
            currdummy = currdummy.next
            curr1 = curr1.next
        
        while curr2!=None:
            currdummy.next = curr2
            currdummy = currdummy.next
            curr2 = curr2.next
        
        
        return dummy.next
        
        
        
        
         
