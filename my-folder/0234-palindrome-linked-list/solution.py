# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if not head or not head.next: return True

        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            if fast:
                slow = slow.next
        
        mid = slow
        # reverse ll from end to mid.next
        if not fast:
            p1 = mid.next
        else:
            p1 = mid
        prev = None
        while p1:
            # None 2 1
            temp = p1.next # temp = 1
            p1.next = prev # p1.next = None 2 -> None
            prev = p1
            p1 = temp
        # match ll1 with ll2
        mid.next = None
        ll2 = prev
        ll1 = head
        while ll1 and ll2:
            if ll1.val != ll2.val:
                return False
            ll1 = ll1.next
            ll2 = ll2.next
                
        if ll1:
            return False
        if ll2:
            return False
        
        return True


