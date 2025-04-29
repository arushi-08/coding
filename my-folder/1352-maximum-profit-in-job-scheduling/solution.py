class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        # n jobs where every job is scheduled to be done from starttime to endtime
        # profit[i]
        # maxprofit - no 2 jobs in subset with overlapping time range

        # starttime = [1,2,3,3]
        # endtime   = [3,4,5,6]
        # profit = [50,10,40,70]

        """
        dp = 
        pick, not pick
        """

        jobs = [[s, e, p] for s, e, p in zip(startTime, endTime, profit) ]
        jobs.sort()

        new_start_times = [e[0] for e in jobs]

        # def helper(idx, prev_pick_idx):
        #     if idx == len(jobs):
        #         return 0
            
        #     current_not_pick = helper(idx+1, prev_pick_idx)

        #     next_idx = bisect.bisect_left(new_start_times, 
        #         jobs[idx][1] 
        #     )
        #     current_pick = helper(next_idx, idx) + jobs[idx][2]

        #     return max(
        #         current_not_pick, current_pick
        #     )

        n = len(jobs)
        dp = [0] * (n+1)

        for i in range(n-1, -1, -1):
            
            start, end, curr_profit = jobs[i]
            
            next_idx = bisect.bisect_left( new_start_times, end )
            
            pick = dp[next_idx] + curr_profit
            not_pick = dp[i+1]

            dp[i] = max(not_pick, pick)

        return dp[0]

