from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000" : return 0
        if "0000" in deadends: return -1
        
        neighbors = {str(i): [str((i+1)%10), str((i-1)%10)] for i in range(10)}
        queue = deque()
        queue.append((0, "0000"))
        result = 0
        visited = {"0000"} | set(deadends)
        
        while len(queue):
            result, curr = queue.popleft()
            
            if curr == target:
                return result
            
            for i in range(len(curr)):
                for j in neighbors[curr[i]]:
                    next_move = curr[:i] + j + curr[i+1:]
                    if next_move not in visited:
                        queue.append((result + 1, next_move))
                        visited.add(next_move)
                    
        return -1
        
