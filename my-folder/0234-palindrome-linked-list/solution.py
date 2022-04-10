# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next == None:
            return True
        
#         get to the middle of LL
#         reverse the second half LL
#         compare the 2 halfs
        
        slow = head
        fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        curr2 = slow
        while curr2:
            temp = curr2.next
            curr2.next = prev
            # print("curr2", curr2)
            prev = curr2
            curr2 = temp
        
        while prev and head:
            # print(head, prev)
            if head.val != prev.val:
                return False
            
            head = head.next
            prev = prev.next

        return True
        
        
        
        
        
#         list1 = []
#         curr = head
#         while curr!= None:
#             list1.append(curr.val)
#             curr = curr.next
        
#         l = 0
#         r = len(list1) - 1
#         while(l < r):
#             if list1[l] == list1[r]:
#                 l += 1
#                 r -= 1
#             else:
#                 return False
        
#         return True
