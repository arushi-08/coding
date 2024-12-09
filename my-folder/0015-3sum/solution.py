class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # return all triplets
        # nums[i], nums[j], nums[k]
        ans = set()
        dup = set()
        for i in range(len(nums)):
            if nums[i] in dup:
                continue
            dup.add(nums[i])
            hmap = {}
            for j in range(i+1, len(nums)):
                if nums[j] in hmap and nums[i] + hmap[nums[j]] + nums[j] == 0:
                    ans.add(tuple(sorted([nums[i], hmap[nums[j]], nums[j]])))
                
                hmap[-(nums[i] + nums[j])] = nums[j]
        
        return list(ans)
                

