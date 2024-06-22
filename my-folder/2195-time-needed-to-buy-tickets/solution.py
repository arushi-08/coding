class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        q = deque([(i, t) for i, t in enumerate(tickets)])
        time = 1
        while q:
            i, t = q.popleft()
            t -= 1
            if t:
                q.append((i, t))
            if i == k and not t:
                return time
            time += 1
            
        return time
