class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        nums.sort()

        def binary_search_get_first_equal_or_greater_than_value(val):
            """find first index >= value
            if no such index then len(nums) is index
            """
            st = 0
            ed = len(nums) - 1
            index = len(nums)
            while st < ed:
                mid = (st + ed) // 2
                if nums[mid] >= val:
                    index = mid
                    ed = mid
                else:
                    st = mid + 1
            return st if nums[st] >= val else index
        
        for i in range(1, len(nums)+1):

            k = binary_search_get_first_equal_or_greater_than_value(i)
            
            # if there are N - k (these are all greater indices w greater values than k (as nums is sorted)) equal to current index, return
            if len(nums) - k == i:
                return i

        return -1
