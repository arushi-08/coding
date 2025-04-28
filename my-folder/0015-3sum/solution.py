class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # given int array nums
        # return all triplets [nums[i], n] sum to 0

        # -4,-1,-1,0,1,2
        """
        if num[i] < 0 -> nums[ed] > 0

        """
        nums.sort()
        result = set()
        print('nums', nums)
        for i in range(len(nums)-1):

            st = i+1
            ed = len(nums)-1
            print(i)

            while st < ed:
                currsum = nums[i] + nums[st] + nums[ed]
                if currsum == 0:
                    result.add(tuple(sorted( [nums[i], nums[st], nums[ed]] )))
                    st += 1
                    ed -= 1
                elif currsum > 0:
                    ed -= 1
                else:
                    st += 1
        
        return list(result)

