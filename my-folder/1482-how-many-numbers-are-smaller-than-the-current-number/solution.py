class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
#         # nums < curr element => sort array find numbers position
        
        copy_nums = nums.copy()
        copy_nums.sort()
        answer = []
        for num in nums:
            answer.append(copy_nums.index(num))
        return answer
