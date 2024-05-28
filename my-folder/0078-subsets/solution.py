class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []

        def recursion(nums, index, res):

            if index == len(nums):
                ans.append(res)
                return
            
            recursion(nums, index + 1, res)
            recursion(nums, index + 1, res + [nums[index]])

        recursion(nums, 0, [])

        return ans
            

