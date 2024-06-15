# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr1 = l1
        curr2 = l2
        ansnode = ListNode()
        curr = ansnode
        while curr1 and curr2:
            curr.val += curr1.val + curr2.val
            if curr1.next or curr2.next:
                curr.next = ListNode()
            if curr.val > 9:
                value = curr.val
                curr.val =  value % 10
                curr.next = ListNode(value // 10)
            curr1 = curr1.next
            curr2 = curr2.next
            curr = curr.next
        
        def helper(curr, curr1):

            while curr1:
                curr.val += curr1.val
                if curr1.next:
                    curr.next = ListNode()
                if curr.val > 9:
                    value = curr.val
                    curr.val =  value % 10
                    curr.next = ListNode(value // 10)
                curr1 = curr1.next
                curr = curr.next
            return curr

        curr = helper(curr, curr1)
        
        curr = helper(curr, curr2)


        return ansnode

