# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """convert ll to map"""
        curra = headA
        lena = 0
        while curra:
            lena += 1
            curra = curra.next

        currb = headB
        lenb = 0
        while currb:
            lenb += 1
            currb = currb.next

        curra = headA
        while lena > lenb:
            # move forward in lena
            curra = curra.next
            lena -= 1
        
        currb = headB
        while lenb > lena:
            # move forward in lena
            currb = currb.next
            lenb -= 1

        if lena == lenb:
            while curra and currb:
                if curra == currb:
                    return curra
                
                curra = curra.next
                currb = currb.next
