class Solution:
    def countValidSelections(self, nums: List[int]) -> int:

        zeros = nums.count(0)
        if zeros == 0:
            return 0

        non_zeros_og = len(nums) - zeros

        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                
                for direction in [1, -1]:
                    non_zeros = non_zeros_og
                    nums_copy = nums.copy()
                    curr = i
                    while non_zeros and 0 <= curr < len(nums):
                        if nums_copy[curr] > 0:
                            nums_copy[curr] -= 1
                            if nums_copy[curr] == 0:
                                non_zeros -= 1 
                                # print(
                                #     'i', i, 'curr',curr,
                                #     'non_zeros', non_zeros, 
                                #     'nums_copy', nums_copy
                                # )
                            direction = -direction
                        curr += direction
                    if not non_zeros:
                        ans += 1
                        
        return ans
