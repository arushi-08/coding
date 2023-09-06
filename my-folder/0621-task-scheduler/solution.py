from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        busy_time = len(tasks)
        hmap = Counter(tasks)
        freq = list(hmap.values())
        freq.sort()
        max_freq = freq.pop()
        idle_time = (max_freq - 1) * n

        while freq and idle_time > 0:
            idle_time -= min(max_freq-1, freq.pop())
        idle_time = max(idle_time, 0)
        return busy_time + idle_time
