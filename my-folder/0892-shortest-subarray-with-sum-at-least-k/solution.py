from collections import deque
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # p[j] - p[i] >= k
        # p[j] - k >= p[i]
        psum = 0
        queue = deque()
        queue.append((0,-1))
        res = len(nums)+1
        for i in range(len(nums)):
            psum += nums[i]
            while queue and psum - k >= queue[0][0]:
                _, idx = queue.popleft()
                res = min(res, i - idx)
            while queue and psum < queue[-1][0]:
                queue.pop()
            queue.append((psum, i))
        
        if res == len(nums) + 1 : return -1
        return res


