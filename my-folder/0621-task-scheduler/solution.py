from heapq import heapify, heappop, heappush
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        if not tasks: return 0
        cooltime = n

        freq2 = [-v for k,v in Counter(tasks).items()]
        heapify(freq2)
        queue = deque()
        time = 0

        while freq2 or queue:
            time += 1
            if freq2:
                currfreq = heappop(freq2) + 1
                if currfreq:
                    queue.append((currfreq, time + cooltime))
            if queue and queue[0][1] <= time:
                next_freq , _ = queue.popleft()
                heappush(freq2, next_freq)
            
        return time





