from collections import deque
class Solution:
    
    def openLock(self, deadends: List[str], target: str) -> int:
        # move: turning 1 wheel 1 slot
        # graph: {digits: neighbouring digits}
        
        if "0000" in deadends: return -1
        
        graph = {}
        for i in range(10):
            if i == 0:
                graph['0'] = ['9', '1']
            elif i == 9:
                graph['9'] = ['8', '0']
            else:
                graph[str(i)] = [str(i-1), str(i+1)]
        
        visited = set(deadends)
        queue = deque()
        queue.append(('0000', 0))
        visited.add('0000')
        
        while queue:
            curr, moves = queue.popleft()
            if curr == target:
                return moves
            
            for i in range(len(curr)):
                for neighbor in graph[curr[i]]:
                    next_turn = curr[:i] + neighbor + curr[i+1:]
                    
                    if next_turn not in visited:
                        queue.append((next_turn, moves + 1))
                        visited.add(next_turn)
                    
                    
        return -1
                    
        
