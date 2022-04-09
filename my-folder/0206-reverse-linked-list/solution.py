# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return head
        
        prev = None
        curr = head
        curr1 = head
        while(curr!= None and curr.next!=None):
            
            temp = curr1.next
            curr1.next = prev
            curr = temp.next
            temp.next = curr1
            prev = temp
            curr1 = curr
            
            # print(prev)
        
        if curr1 != None:
            curr1.next = prev
        else:
            return prev
        
        return curr1
            
