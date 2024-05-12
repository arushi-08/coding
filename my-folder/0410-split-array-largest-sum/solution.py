class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        

        start = max(nums)
        end = sum(nums)
        maxans = end

        while start <= end:
            mid = (start + end)//2
            # print("mid", mid)
            splits = [0] * k
            all_done = 0
            j = 0
            for i in range(k):
                sum_i = 0
                while j < len(nums) and sum_i + nums[j] <= mid:
                    sum_i += nums[j]
                    j += 1

                splits[i] = sum_i
                # print("mid", mid, "j", j, "splits", splits)
                if j == len(nums):
                    # print("splits", splits)
                    all_done = i
                    break
            if j == len(nums):
                
                maxans = min(maxans, max(splits))
                
                end = mid - 1

            elif j < len(nums):
                start = mid + 1
            else:
                end = mid - 1
        
        return maxans
            
            

