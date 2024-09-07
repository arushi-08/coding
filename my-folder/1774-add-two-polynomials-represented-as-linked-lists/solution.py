# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        # [[2,2],[4,1],[3,0]]
        # 2x**2 + 4x + 3

        # [[3,2],[-4,1],[-1,0]]
        # 3x**2 - 4x - 1

        # compare the power of both ploy1 ptr & poly2 ptr
        # if same
        # add the coefficient
        # else:
        #   ptr = ptr.next for the bigger power poly

        # add the remaining terms of the other poly


        poly1_ptr = poly1
        poly2_ptr = poly2

        prev = PolyNode()
        prevhead = prev
        prev.next = poly1_ptr

        while poly1_ptr and poly2_ptr:

            p1_power = poly1_ptr.power
            p2_power = poly2_ptr.power

            if p1_power == p2_power:
                poly1_ptr.coefficient += poly2_ptr.coefficient

                if poly1_ptr.coefficient == 0:
                    prev.next = poly1_ptr.next
                else:
                    prev.next = poly1_ptr
                    prev = prev.next

                poly1_ptr = poly1_ptr.next
                poly2_ptr = poly2_ptr.next

            # p1 = x**5, p2 = x**3
            elif p1_power > p2_power:
                prev.next = poly1_ptr
                poly1_ptr = poly1_ptr.next
                prev = prev.next
            # p1 = x**3, p2 = x**5+x**3
            else:
                prev.next = PolyNode(poly2_ptr.coefficient,poly2_ptr.power)
                prev = prev.next
                poly2_ptr = poly2_ptr.next

        if poly2_ptr:
            prev.next = poly2_ptr
        
        if poly1_ptr:
            prev.next = poly1_ptr

        return prevhead.next

            


