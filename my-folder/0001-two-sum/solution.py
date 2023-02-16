class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        secondsum_map = {}
        for i in range(len(nums)):
            second_element = target - nums[i]
            if second_element in secondsum_map:
                return [secondsum_map[second_element], i]
            secondsum_map[nums[i]] = i
        
        return -1
