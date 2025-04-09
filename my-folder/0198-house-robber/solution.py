class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # nums = [1,2,3,1]
        # goal: return max value from non adj idx

        after_money = [0] * 2
        curr_money = [0] * 2

        for i in range(len(nums)-1,-1,-1):
            curr_money[1] = after_money[0]
            curr_money[0] = max(after_money[1] + nums[i], after_money[0])

            after_money = curr_money[:]
        
        return after_money[0]
