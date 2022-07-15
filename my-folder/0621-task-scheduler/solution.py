from collections import Counter
from heapq import heappush, heappop
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """create freq dict of char array => {A:3, B:3}
           loop over freq dict keys => do A then B, then A but before A idle time
        """
        
        freq_dict = Counter(tasks)
        max_heap = []
        for task, freq in freq_dict.items():
            heappush(max_heap, (0, -freq, task))
        time = 0
        while max_heap:
            task_execution_time = max_heap[0][0]
            if task_execution_time <= time:
                task_time, freq, task = heappop(max_heap)
                if freq + 1 < 0 :
                    heappush(max_heap, (task_time + n + 1, freq + 1,task))
            time += 1
        
        return time
            
