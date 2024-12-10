class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        idea : binary search to find the mid point in nums1 that is last element going into 1st half of nums1+nums2 array
        start with assuming that half of half of the nums1+nums2 array would be in nums1 and the other half is in nums2
        l1 r1
        l2 r2
        main conditions: if r1_first < l2_second and r2_first < l1_second
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        st = 0
        ed = len(nums1)
        half = (len(nums1) + len(nums2) + 1)//2
        while st <= ed:
            mid1 = (st + ed) // 2
            mid2 = half - mid1

            l1, l2 = self.get_l1_l2(mid1, mid2, nums1, nums2)
            r1, r2 = self.get_r1_r2(mid1, mid2, nums1, nums2)

            if l1 <= r2 and l2 <= r1:
                if (len(nums1) + len(nums2)) & 1 == 0:
                    return (min(r1,r2) + max(l1,l2))/2
                return max(l1, l2)
            if l1 > r2:
                ed = mid1 - 1 # move ed to left as nums1 ed is pointing to greater element and we need less of nums1
            elif l2 > r1:
                st = mid1 + 1
        
        return 0
    
    def get_l1_l2(self, mid1, mid2, nums1, nums2):
        l1, l2 = -float('inf'), -float('inf')
        if mid1 > 0:
            l1 = nums1[mid1-1]
        if mid2 > 0:
            l2 = nums2[mid2-1]
        return l1, l2

    def get_r1_r2(self, mid1, mid2, nums1, nums2):
        r1, r2 = float('inf'), float('inf')
        if mid1 < len(nums1):
            r1 = nums1[mid1]
        if mid2 < len(nums2):
            r2 = nums2[mid2]
        return r1, r2


