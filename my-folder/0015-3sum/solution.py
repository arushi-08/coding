class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        set1 = set()
        set2 = {}
        ans = set()
        for i in range(len(nums)):
            if i not in set1:
                set1.add(i)
                for j in range(i+1, len(nums)):
                    remain = -(nums[i] + nums[j])
                    if remain in set2 and set2[remain] == i:
                        ans.add(tuple(sorted([nums[i], nums[j], remain])))
                    set2[nums[j]] = i
        
        return list(ans)


