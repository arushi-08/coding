class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        # start with initial positive value
        # startvalue
        # calculate step by step sum of startvalue plus elements in nums
        # from left to right

        # return minimum positive value of start_value such that the step by step sum is never < 1
        # what's the max negative = -6
        # what's the positives before the max negative = 2
        # ans is > 4
        neg_sum = 0
        pos_sum = 0
        min_pos_value = 1
        for i in range(len(nums)):
            if nums[i] < 0:
                neg_sum += nums[i]
                print('i', i, 'neg_sum', neg_sum, 'pos_sum', pos_sum)
                min_pos_value = max(min_pos_value, 1 + (-1) * (neg_sum + pos_sum))
                print('min_pos_value', min_pos_value)
            else:
                pos_sum += nums[i]
        
        return max(1, min_pos_value)
