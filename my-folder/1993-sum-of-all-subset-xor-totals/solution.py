class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        subsets = []
        def dfs(res, idx):
            if idx == len(nums):
                subsets.append(res)
                return
            
            dfs(res, idx+1)
            dfs(res + [nums[idx]], idx + 1)
        
        dfs([], 0)
        
        sum_xor_total = 0
        for sub in subsets:
            xor_total = 0
            for n in sub:
                xor_total ^= n
            sum_xor_total += xor_total
        
        return sum_xor_total
