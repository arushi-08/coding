from heapq import heappush, heappop, heapify
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # O(N + klogn)
        heap = []
        for i in range(len(matrix)): #  O(N)
            heap.append((matrix[i][0], i, 0))
            
        heapify(heap) # O(N)
        
        i = 0
        while i < k: # O(klogN)
            curr, row, col = heappop(heap)
            if col + 1 < len(matrix[row]):
                heappush(heap, (matrix[row][col + 1], row, col + 1))
            i += 1
        
        return curr
            
