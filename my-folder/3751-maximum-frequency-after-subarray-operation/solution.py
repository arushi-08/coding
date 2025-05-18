class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        # k_count = nums.count(k)

        # curr_val = None
        # curr_len = 0
        # max_val = 0
        # for i, num in enumerate(nums):
        #     if num == k:
        #         curr_val = None
        #         curr_len = 0
        #     else:
        #         if num == curr_val:
        #             curr_len += 1
        #         else:
        #             curr_val = num
        #             curr_len = 1
                    
        #         max_val = max(max_val, curr_len + k_count )
        
        # return max_val
        
        # kadane's algo - how?

        # do a search for each value (1 through 50)
        # represented as x
        # we can imagine that all nums[i] = X have a value of 1
        # we can imagine any number that != X or k will have a value of 0
        # we can imagine any number with a value == k has a value of -1


        # kadane's algo:
            # 2 choices:
                # 1. either extend the current subarray
                # 2. start a new subarray

        k_freq = nums.count(k)

        unique_vals = set(nums)

        max_duplicates = 0

        for val in unique_vals:
            if val == k:
                continue

            currlen = 0
            maxlen = 0
            for num in nums:
                if val == num:
                    currlen += 1
                elif num == k:
                    currlen -= 1 # this is done because k_freq is added in the end, so we subtract 1 in the current subarray
                currlen = max(currlen, 0)
                maxlen = max(maxlen, currlen)
            
            max_duplicates = max(
                max_duplicates, maxlen
            )
        
        return max_duplicates + k_freq
        
        
        





