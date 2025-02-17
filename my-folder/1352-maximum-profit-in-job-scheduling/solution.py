class Solution:
    def jobScheduling(self, starttime: List[int], endtime: List[int], profit: List[int]) -> int:
        
        # find the last non-conflicting job with current job
        jobs = [(start, end, p) for start, end, p in zip(starttime, endtime, profit)]

        jobs.sort(key = lambda x: x[1])
        self.memo = {}

        return self.maxProfitJobs(jobs, len(jobs)-1)
    
    def maxProfitJobs(self, jobs, n):

        if n < 0:
            return 0
        
        if n == 0:
            return jobs[n][2]
        
        if n in self.memo:
            return self.memo[n]
        
        i = self.findLastNonConflictJob(jobs, n)
        # print(i,n)
        include = self.maxProfitJobs(jobs, i) + jobs[n][2]
        exclude = self.maxProfitJobs(jobs, n-1)

        self.memo[n] = max(include, exclude)
        return self.memo[n]
    
    def findLastNonConflictJob(self, jobs, n):
        
        start = 0
        end = n-1
        ans = -1
        while start <= end:
            mid = (start + end)//2
            if jobs[mid][1] <= jobs[n][0]:
                ans = mid
                start = mid + 1
            else:
                end = mid - 1

        return ans

