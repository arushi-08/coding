# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if not head: return False
        if not head.next: return True
        slow = head
        fast = head
        head2 = None
        while slow and fast and fast.next:
            
            fast = fast.next.next
            
            if not fast or not fast.next:
                head2 = slow.next
                slow.next = None
                
            slow = slow.next
#         2 -> 1 -> 0
        curr = head2
        prev = None
        while curr:
            
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        head2 = prev
        
        curr1 = head
        curr2 = head2
        
        while curr1 and curr2:
            if curr1.val != curr2.val:
                return False
            curr1 = curr1.next
            curr2 = curr2.next
        
        return True
            
            
        
