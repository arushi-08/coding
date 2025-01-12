class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # 2 sorted arrays - m and n size
        # return median of 2 sorted arr's
        # compare l1 w r2, l2 w r1

        # find mid1 point
        # mid2 = (m+n)//2 - mid1
        # find l1, l2, r1,r2 using mid1, mid2
        # if l1  < r1 and l2 < r1
        # l1 r2
        # l2 r2
        # 1 3
        # 2 4
        # then return l2+r1//2
        # 1 3
        # 2 inf
        # return max(l1,l2)
        # 2 3
        # 1
        # 3 4
        # 2

        def get_l_r(mid, nums):
            l, r = -float('inf'), float('inf')
            if 0 < mid:
                l = nums[mid-1] #
            if mid < len(nums):
                r = nums[mid]
            return l, r


        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        st = 0
        ed = len(nums1) #
        totallen = len(nums1) + len(nums2)
        halflen = (totallen+1)//2 #
        while st <= ed:
            mid1 = (st + ed)//2
            mid2 = halflen - mid1
            l1, r1 = get_l_r(mid1, nums1)
            l2, r2 = get_l_r(mid2, nums2)

            if l1 <= r2 and l2 <= r1:
                if totallen & 1 == 0:
                    return (max(l1,l2) + min(r1,r2))/2 #
                return max(l1, l2)

            if r1 < l2: # more of nums1
                st = mid1 + 1
            else:
                ed = mid1 - 1
        
        return 0
        


