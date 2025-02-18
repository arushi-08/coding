

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums2, nums1 = nums1, nums2
        
        total_len = len(nums1) + len(nums2)
        half_len = (total_len+1)//2
        # [1,2,3]
        # [5,6,7]
        # half len = 2, mid = 1, nums2mid = 0
        st = 0
        end = len(nums1)

        while st <= end:
            mid = (st + end) // 2
            nums2mid = half_len - mid

            l1, r1 = self.get_l_r(nums1, mid)
            l2, r2 = self.get_l_r(nums2, nums2mid)

            if l1 <= r2 and l2 <= r1:
                # print(l1,  r1, l2, r2)
                if total_len & 1 == 0:
                    return (max(l1, l2) + min(r1, r2))/2
                return max(l1,l2)
            
            if l2 > r1:
                # 6 > 4, pick more of nums1
                st = mid + 1
            else:
                end = mid - 1
        
        return 0

    
    def get_l_r(self, nums, mid):
        n = len(nums)
        l,r = -float('inf'), float('inf')
        if 0 < mid:
            l = nums[mid-1]
        if mid < n:
            r = nums[mid]
        return l, r

