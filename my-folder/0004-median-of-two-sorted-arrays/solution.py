class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        half_len = length of 1st half of array (if array is odd, left half is longer of the 2 halves) => (totallen + 1)/2
        l = nums[mid-1]
        r = nums[mid]
        arr1 = l1.  r1
        arr2 = l2.  r2
        partition the 2 arrays such that all elements in the left half are smaller than all elements in the right half 
        mid condition:
            if l1 <= r2 and l2 <= r1:
                if total is even:
                    return (max(l1,l2) + min(r1,r2))/2
                return max(l1,l2)
            if l1 > r2:
                we have moved too much to right side, need to move left
                ed = mid1 - 1
            else:
                st = mid1 + 1
        """

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        st = 0
        ed = len(nums1)
        total_len = len(nums1) + len(nums2)
        half_len = (total_len+1) // 2
        
        while st <= ed:
            mid1 = (st + ed) // 2
            mid2 = half_len - mid1
            l1, r1 = self.get_l_r(nums1, mid1)
            l2, r2 = self.get_l_r(nums2, mid2)

            if l1 <= r2 and l2 <= r1:
                if total_len & 1 == 0:
                    return (max(l2, l1) + min(r1, r2))/2
                return max(l1,l2)
            
            if l1 > r2:
                ed = mid1 - 1
            else:
                st = mid1 + 1
        
    
    def get_l_r(self, nums, mid):

        l = -float('inf')
        r = float('inf')
        if 0 <= mid - 1:
            l = nums[mid-1]
        if mid < len(nums):
            r = nums[mid]
        return l, r
