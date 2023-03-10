class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        set1 = set()
        hmap = {}
        ans = set()
        for i in range(len(nums)):
            if nums[i] not in set1:
                set1.add(nums[i])
                for j in range(i+1, len(nums)):
                    seen_j = -(nums[i] + nums[j])
                    if seen_j in hmap and hmap[seen_j]==i:
                        ans.add(tuple(sorted([nums[i], nums[j], seen_j])))
                    hmap[nums[j]] = i
        
        return ans
