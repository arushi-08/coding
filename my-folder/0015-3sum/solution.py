class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        i = 0
        hm = {}
        ans = set()
        dups = set()
        while i < len(nums):
            if i not in dups:
                dups.add(i)
                for j in range(i+1, len(nums)):
                    remain = -nums[i] -nums[j]
                    if remain in hm and hm[remain] == i:
                        ans.add(tuple(sorted((remain, nums[i], nums[j]))))
                    hm[nums[j]] = i
            i += 1

        return ans
