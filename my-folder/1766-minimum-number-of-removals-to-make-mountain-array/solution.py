class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        
        # 2,1,1,5,6,2,3,1
        # 1,5,6,3,1

        # remove elements to make 1 mountain
        # use LIS to find ascending elements

        # let's begin writing what needs to be done
        # have to find mountain
        # max mountain that can be created
        # [4,3,2,1,1,2,3,1]

        
        min_moves = float('inf')
        left_lis = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    left_lis[i] = max(left_lis[i], left_lis[j]+1)
        
        right_lis = [1] * len(nums)
        for i in range(len(nums)-1,-1,-1):
            for j in range(len(nums)-1,i,-1):
                if nums[j] < nums[i]:
                    right_lis[i] = max(right_lis[i], right_lis[j]+1)
        
        for i in range(1, len(nums)-1):
            if left_lis[i] > 1 and right_lis[i] > 1:
                min_moves = min(min_moves, len(nums)- (
                    left_lis[i] + right_lis[i] - 1
                    )
                )

        return min_moves
