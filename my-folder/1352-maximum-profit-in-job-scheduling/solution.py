class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # we have n jobs
        # no overlap 
        # max profit
        # use heap to track max current profit
        # but current max may not be global max
        # dp?
        times = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])

        n = len(times)

        dp = [0] * (n+1)
        end_times = [t[1] for t in times]
        for i in range(1, n+1):
            
            # don't take current profit
            dp[i] = dp[i-1]

            idx_end_before_i_start = bisect.bisect_right(end_times, times[i-1][0]) 
            
            # choice
            dp[i] = max(dp[i], dp[idx_end_before_i_start] + times[i-1][2]) 

        return dp[-1]

"""
why can we memoize this solution?
is last_used_end_time repeating? is that why?
"""
