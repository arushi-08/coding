import bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        # return max profit such that no 2 jobs are overlapping
        # dp

        job_times = [[st, ed, p] for st, ed, p in zip(startTime, endTime, profit)]
        job_times.sort(key=lambda x:x[0])

        starts = [j[0] for j in job_times]
        ends = [j[1] for j in job_times]

        next_index = []
        for end in ends:
            j = bisect.bisect_left(starts, end)
            next_index.append(j)

        n = len(job_times)
        dp = [0] * (n+1)

        for i in range(n-1,-1,-1):

            take_profit = dp[next_index[i]] + job_times[i][2]
            skip_profit = dp[i+1]
            dp[i] = max(take_profit, skip_profit) 
        
        return dp[0]



