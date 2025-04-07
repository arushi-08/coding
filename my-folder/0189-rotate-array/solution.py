class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        if k == 0 or not nums: return
        self.reverse(nums, 0, n-1)
        k %= n
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)

    def reverse(self, nums, st, ed):
        while st < ed:
            nums[st], nums[ed] = nums[ed], nums[st]
            st += 1
            ed -= 1

        # [-1,-100,3,99]
        # new_pos = 2
        # temp = 3
        # nums[3] = 1
        # _,_,_,1,..
        # curr = 4
        # i = 3
        # new_pos = 6
        # temp = 7
        # nums[6] = 4
        # 

            

# 1,2,3,4,5,6
# _,2,5,4,1,6
# 3,2,5,4,1,6
# 
# [3,4,5,6,1,2]
# k=4
# 6,5,4,3,2,1
# reverse substr, 

# 1,2,3,4,5,6
