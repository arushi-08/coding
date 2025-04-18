# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # given 2 non empty linked lists representing 2 non-negative integers.
        # digits are stored in reverse order

        # 2 -> 4 -> 3
        # 5 -> 6 -> 4
        # 7 -> 0 -> 8

        # 2 things:
        # add number, number < 10 -> new node with val
        # number >= 10 -> store remainder in new node, carry 1 in a varible for next new node
        # 

        result_head = ListNode(0)
        curr = result_head
        carry = 0
        
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            addval = v1 + v2 + carry
            carry = 0
            if addval >= 10:
                carry = addval // 10
                addval %= 10
            
            curr.next = ListNode(addval)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return result_head.next
            
        
