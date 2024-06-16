class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        
        if not nums or len(nums) < 2: return 0
        ans = 0
        count = 0
        hmap = defaultdict(list)
        
        for i in range(len(nums)-1,-1,-1):
            hmap[nums[i] % diff].append(nums[i])

        
        for k, v in hmap.items():
            if len(v) < 3:
                continue
            for i in range(len(v)-2):
                if v[i] == v[i+1] + diff and v[i+1] == v[i+2] + diff:
                    ans += 1
        
        return ans
