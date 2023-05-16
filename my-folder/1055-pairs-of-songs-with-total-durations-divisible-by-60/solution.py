from collections import defaultdict
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        seen = defaultdict(int)
        count = 0
        for i in range(len(time)):
            count += seen[(60 - time[i]%60) % 60]
            seen[time[i]%60] += 1

        return count
