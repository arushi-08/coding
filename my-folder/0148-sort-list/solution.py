# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next: return head
        
        def getmid(head):
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        mid = getmid(head)
        left = head
        right = mid.next
        mid.next = None
        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)
 
    def merge(self, left, right):
        answer = ListNode()
        currans = answer
        while left and right:
            if left.val < right.val:
                currans.next = left
                left = left.next
            else:
                currans.next = right
                right = right.next
            currans = currans.next

        if left:
            currans.next = left
        
        if right:
            currans.next = right
        
        return answer.next




