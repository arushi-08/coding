class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        tasks = sorted(zip(startTime, endTime, profit))
        startTimes = [t[0] for t in tasks]

        self.memo = {}

        return self.helper(tasks, startTimes, 0)

    def helper(self, tasks, startTimes, idx):

        if idx == len(tasks):
            return 0
        if idx in self.memo:
            return self.memo[idx]

        # find the 1st task that has start time > idx end time
        next_idx = bisect.bisect_left(startTimes, tasks[idx][1])

        skip = self.helper(tasks, startTimes, idx+1)

        self.memo[idx] = max(
            skip,
            self.helper(tasks, startTimes, next_idx) + tasks[idx][2]
        )
        
        return self.memo[idx]
