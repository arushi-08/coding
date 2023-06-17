from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        # bfs
        queue = deque()
        queue.append((startGene, 0))
        visited = set()
        while len(queue):
            curr, currcount = queue.popleft()
            for moves in bank:
                if moves not in visited:
                    
                    count = 0
                    for c1,c2 in zip(curr, moves):
                        if c1 != c2:
                            count+=1
                    if count > 1:
                        continue
                    visited.add(moves)
                    if moves == endGene:
                        return currcount + 1
                    queue.append((moves, currcount+1))

        if curr == endGene: return currcount
        return -1

