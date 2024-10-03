class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        st = 0
        ed = 0
        maxqueue = deque() # mono decreasing
        minqueue = deque() # mono increasing

        ans = 0
        while ed < len(nums):

            while st < ed and maxqueue and minqueue and nums[maxqueue[0]] - nums[minqueue[0]] > limit:
                if st == maxqueue[0]:
                    maxqueue.popleft()
                if st == minqueue[0]:
                    minqueue.popleft()
                st += 1

            while maxqueue and nums[maxqueue[0]] < nums[ed]:
                maxqueue.popleft()
            while maxqueue and nums[maxqueue[-1]] < nums[ed]:
                maxqueue.pop()
            maxqueue.append(ed)
            
            while minqueue and nums[minqueue[0]] > nums[ed]:
                minqueue.popleft()
            while minqueue and nums[minqueue[-1]] > nums[ed]:
                minqueue.pop()
            minqueue.append(ed)

            if nums[maxqueue[0]] - nums[minqueue[0]] <= limit:
                # print(maxqueue, minqueue, st, ed, ed-st+1)
                ans = max(ans, ed - st + 1)
            
            ed += 1

        return ans


