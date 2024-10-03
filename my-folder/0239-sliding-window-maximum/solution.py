class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        st = 0
        ed = 0
        queue = deque()
        ans = []

        while ed < len(nums):
            
            while ed < st + k and ed < len(nums):
                while queue and nums[ed] > nums[queue[0]]:
                    queue.popleft()
                while queue and nums[ed] > nums[queue[-1]]:
                    queue.pop()
                queue.append(ed)

                ed += 1

            # print(st, ed, queue)
            if queue:
                ans.append(nums[queue[0]])
            st += 1

            if queue and queue[0] == st - 1:
                queue.popleft()

        return ans




