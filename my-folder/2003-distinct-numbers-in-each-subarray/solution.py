class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        
        # given int arr, and k
        # construct array ans of size n-k+1
        # ans[i] is num of distinct nums in subarr nums[i:i+k-1]

        # sliding window
        # check num_distinct in first k nums, then check next num

        max_val = max(nums)
        distinct_freq = [0] * (max_val+1)
        min_length = min(k, len(nums))
        distinct_count = 0

        def add_distinct_freq(distinct_freq, distinct_count, idx):
            if distinct_freq[idx] == 0:
                distinct_count += 1
            distinct_freq[idx] += 1
            return distinct_freq, distinct_count

        def remove_distinct_freq(distinct_freq, distinct_count, idx):
            distinct_freq[idx] -= 1
            if distinct_freq[idx] == 0:
                distinct_count -= 1
            return distinct_freq, distinct_count


        for i in range(min_length):
            distinct_freq, distinct_count = add_distinct_freq(
                distinct_freq, distinct_count, nums[i]
                )

        ans = [distinct_count]
        if len(nums) <= k: 
            return ans
        
        start = 0
        for end in range(k, len(nums)):
            distinct_freq, distinct_count = remove_distinct_freq(
                distinct_freq, distinct_count, nums[start]
                )
            
            distinct_freq, distinct_count = add_distinct_freq(
                distinct_freq, distinct_count, nums[end]
                )
            ans.append(distinct_count)
            start += 1
        
        return ans

