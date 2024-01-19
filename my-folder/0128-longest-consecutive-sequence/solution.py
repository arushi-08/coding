
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums.sort()
        answer = 0
        currans = 0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                continue
            if nums[i] + 1 == nums[i+1]:
                currans += 1
            else:
                if currans:
                    currans += 1
                answer = max(answer, currans)
                currans = 0
        # if currans:
        #     return max(answer, currans+1)
        return max(answer, currans+1)


