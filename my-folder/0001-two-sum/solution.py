class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # 2, 9, 20,35. 3, 5, 9
        hm = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hm:
                return [i, hm[complement]]
            hm[nums[i]] = i
    
        return []
