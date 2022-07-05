# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class MinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0
    
    def insert(self, val):
        self.heap_list.append(val)
        self.current_size += 1
        self.bubble_up(self.current_size)
    
    def bubble_up(self, idx):
        while idx // 2 > 0: 
            if self.heap_list[idx // 2][0] > self.heap_list[idx][0]:
                self.heap_list[idx // 2], self.heap_list[idx] = self.heap_list[idx], self.heap_list[idx // 2]
            else:
                break
            idx //= 2
    
    def delete(self):
        root = self.heap_list[1]
        self.heap_list[1] = self.heap_list[-1]
        self.heap_list.pop()
        self.current_size -= 1
        self.bubble_down()
        return root
    
    def bubble_down(self):
        idx = 1
        while (idx * 2) <= self.current_size:
            min_child_idx = self.get_min_child_idx(idx)
            
            if self.heap_list[idx][0] > self.heap_list[min_child_idx][0]:
                self.heap_list[idx], self.heap_list[min_child_idx] = self.heap_list[min_child_idx], self.heap_list[idx]
            else:
                break
            idx = min_child_idx
    
    def get_min_child_idx(self, idx):
        if (2*idx)+1 > self.current_size:
            return 2*idx
        
        if self.heap_list[(2*idx)+1][0] > self.heap_list[(2*idx)][0]:
            return 2*idx
    
        return (2*idx) + 1
    
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = MinHeap()
        for idx, node in enumerate(lists):
            if node:
                heap.insert((node.val, idx))
                lists[idx] = lists[idx].next
        
        result = ListNode()
        curr = result
        while heap.current_size > 0:
            val, idx = heap.delete()
            curr.next = ListNode(val)
            curr = curr.next
            if lists[idx]:
                heap.insert((lists[idx].val, idx))
                lists[idx] = lists[idx].next
        
        return result.next
        
        
