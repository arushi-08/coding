class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        print(nums)
        left = 0
        right = len(nums) - 1
        result = [0]*len(nums)
        for i in range(len(nums)-1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                answer = nums[left]
                left += 1
            else:
                answer = nums[right]
                right -= 1
            result[i] = answer*answer
        return result
