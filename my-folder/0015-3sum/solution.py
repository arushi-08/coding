class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans = set()
        dup = set()
        for i in range(len(nums)):
            hmap = {}
            if nums[i] in dup:
                continue
            dup.add(nums[i])
            for j in range(i+1, len(nums)):
                term = -(nums[i] + nums[j])
                if term in hmap:
                    ans.add(tuple(sorted([hmap[term], nums[i], nums[j]])))
                
                hmap[nums[j]] = nums[j]
        
        res = []
        for i in ans:
            res.append(list(i))
        
        return res
