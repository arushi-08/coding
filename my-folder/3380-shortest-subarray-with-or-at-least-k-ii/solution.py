class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        # nums = [1,2,3], k = 2
        # array is called special if bitwise OR of all elements is at least k
        
        if max(nums) >= k: return 1

        def bits_update(bits, n, diff):
            for i in range(32):
                if n & (1 << i): # checking which all bits in n are set
                    bits[i] += diff
        
        def bit_to_int(bits):
            ans = 0
            for i in range(32):
                if bits[i]:
                    ans += (1 << i)
            return ans

        l = 0
        bits = [0] * 32
        res = float('inf')
        
        for r in range(len(nums)):
            bits_update(bits, nums[r], 1)
            curr_or = bit_to_int(bits)
            
            while l <= r and curr_or >= k:
                res = min(res, r-l+1)
                bits_update(bits, nums[l], -1)
                curr_or = bit_to_int(bits)
                l += 1
        
        return res if res != float('inf') else -1


