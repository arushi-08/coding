class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        
        if len(nums) <= 2*k: return []

        i = 0 
        decreasing_map = {}
        while i < len(nums)-k:
            decreasing = 0
            while i + 1 < len(nums) and nums[i] >= nums[i+1] and k > 1:
                decreasing += 1
                i += 1
                if decreasing >= k:
                    decreasing_map[i] = 1
            if decreasing:
                decreasing += 1
            if decreasing >= k or k == 1:
                decreasing_map[i+1] = 1
            i += 1

        i = len(nums)-1
        increasing_map = {}
        while i >= 0:
            increasing = 0
            while i - 1 >= 0 and nums[i] >= nums[i-1] and k > 1:
                increasing += 1
                i -= 1
                if increasing >= k:
                    increasing_map[i] = 1
            if increasing:
                increasing += 1
            if increasing >= k or k == 1:
                increasing_map[i-1] = 1
            i -= 1
        print('decreasing_map', decreasing_map)
        print('increasing_map', increasing_map)
        i = k
        ans = []
        while i < len(nums):
            if decreasing_map.get(i,0) and increasing_map.get(i,0):
                ans.append(i)
            i += 1
            
        return ans
