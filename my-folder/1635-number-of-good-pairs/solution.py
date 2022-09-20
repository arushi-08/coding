from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
#         nums[i] == nums[j] and i < j
        
#         create a freq map, wherever freq > 1 => check those elements indices
#          freq = 2, good pairs = 1
#           freq = 3, good pairs = 3
#           freq = 4, good pairs = 5
#            1 1 1 1 1
#           0, 1, 3, 6, 10, 15 6C2 ? 6 / 2 * 4
        memo = {}
        def factorial(num):
            if num in [0,1]: return 1
            if num in memo: return memo[num]
            else:
                memo[num] = num * factorial(num-1)
            return memo[num]
            
        def combination(num):
            return int(factorial(num) / (factorial(num-2) * 2))
        
        freq_map = Counter(nums)
        ans = 0
        for i in freq_map:
            if freq_map[i] > 1:
                ans += combination(freq_map[i])
        
        return ans
