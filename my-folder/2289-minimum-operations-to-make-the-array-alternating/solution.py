class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        # given 0-indexed array nums consisting of n positive integers
        # array nums is called alternating if
        # nums[i-2] == nums[i], 2 <= i <= n-i
        # nums[i-1] != nums[i], 1 <= i <= n-1

        # in 1 op, you can choose an index i and change nums[i] into any positive integer

        # 
        # min number of ops to make array alternating
        # i'm thinking of 2 ops at each step
        # either change it to i - 2's element or keep it
        # issue is TC
        # binary search?
        # min ops = 1, FFFFTTTTT
        # max ops = len(nums)

        st = 0
        ed = len(nums)
        res = len(nums)
        while st <= ed:
            mid = (st + ed) // 2
            if self.can_be_alternating(nums, mid):
                res = mid
                ed = mid - 1
            else:
                st = mid + 1
        
        return res
    
    def get_even_odd_freq(self, nums):
        even_freq = {}
        odd_freq = {}
        for i in range(0, len(nums), 2):
            even_freq[nums[i]] = even_freq.get(nums[i], 0) + 1
            if i+1 < len(nums):
                odd_freq[nums[i+1]] = odd_freq.get(nums[i+1], 0) + 1
        return even_freq, odd_freq
    
    def get_max_alternating_idx(self, freq):
        max_v = 0
        max_k = 0
        sec_max_v = 0
        for k, v in sorted(freq.items(), key=lambda x:x[1]):
            sec_max_v = max_v
            max_v = max(max_v, v)
            if max_v == v:
                max_k = k
        return max_k, max_v, sec_max_v

    def get_even_odd_count(self, nums):
        if len(nums) & 1 == 0:
            # even length
            even_count = len(nums)//2
            odd_count = len(nums)//2
        else:
            even_count = (len(nums) + 1)//2
            odd_count = even_count - 1
        
        return even_count, odd_count

    def can_be_alternating(self, nums, mid):
        # even_freq stores elems at even idx and similarly for odd_idx
        # I get max values at odd and even idx
        # i need to check that if these are for the same key
        # then consider the second max value,
        # but if this second max value doesn't exist then? need to assign a new value
        # 
        even_freq, odd_freq = self.get_even_odd_freq(nums)

        if len(even_freq) + len(odd_freq) - 2 > mid:
            return False
        
        max_k_even, max_v_even, sec_max_v_even = self.get_max_alternating_idx(even_freq)
        max_k_odd, max_v_odd, sec_max_v_odd = self.get_max_alternating_idx(odd_freq)
        even_count, odd_count = self.get_even_odd_count(nums)
        
        # what must change, by how much, and under what circumstances?
        if max_k_even != max_k_odd:
            cost = even_count - max_v_even + odd_count - max_v_odd
            return cost <= mid
        
        cost1 = even_count - max_v_even + odd_count - sec_max_v_odd
        cost2 = even_count - sec_max_v_even + odd_count - max_v_odd

        return min(cost1, cost2) <= mid
