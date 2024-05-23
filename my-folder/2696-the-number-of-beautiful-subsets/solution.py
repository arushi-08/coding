from collections import defaultdict
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        
        def helper(count, i):
            if i == len(nums):
                return 1
            
            res = helper(count, i+1)
            if not count[nums[i] - k] and not count[nums[i] + k]:
                count[nums[i]] += 1
                res += helper(count, i+1)
                count[nums[i]] -= 1
            return res

        return helper(defaultdict(int), 0) - 1
