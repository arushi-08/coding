class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        
        st = 0
        maxcount = 0
        # store greater elements in stack
        # store maxcount when greater elements arrive = ed - st
        stack = [0]

        for ed in range(1, len(nums)):

            # while st <= ed and nums[st] < nums[ed]:
            #     st += 1
            
            if nums[ed] >= nums[stack[-1]]:
                stack.append(ed)
            else:
                maxcount = max(maxcount, ed - stack[-1])
        # print('maxcount', maxcount)
        ed = len(nums)-1
        while stack and ed >= 0:
            if nums[stack[-1]] > nums[ed]:
                print(nums[stack[-1]], nums[ed])
                maxcount = max(maxcount, ed - stack[-1] + 1)
                stack.pop()
            else:
                ed -= 1
        return maxcount
