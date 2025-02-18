class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        ans = set()

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            
            start = i+1
            end = len(nums)-1

            while start < end:
                sumval = nums[i] + nums[start] + nums[end]
                if sumval == 0:
                    ans.add((nums[i],nums[start], nums[end]))
                    start += 1
                    end -= 1
                elif sumval < 0:
                    start += 1
                else:
                    end -= 1
        
        return list(ans)
