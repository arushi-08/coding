# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        
        # find values that appear more than once in the list
        # delete nodes that have any of those values
        # 
        # 
        # iterate and store in set the seen value till now

        visited = {}
        curr = head
        prev = ListNode(-1)
        og_prev = prev
        prev.next = curr

        while curr:
            visited[curr.val] = visited.get(curr.val, 0)+1
            curr = curr.next

        curr = head
        while curr:
            while curr and visited[curr.val] > 1:
                prev.next = curr.next
                curr = curr.next
            if curr:
                prev = prev.next
                curr = curr.next

        return og_prev.next


