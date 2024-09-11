class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # 2 sorted arrays
        # either i could use minheap, maxheap to store median as top values
        # but if the arrays length are too different, then median is in 1 of these arrays
        # 
        # 
        # nums1 = [1,3,5,7] nums2 = [2]
        
        # 1st do BS, find the num of elements you can take from 
        # the smaller array from nums1, nums2

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        start = 0
        end = len(nums1)

        half_length = (len(nums1) + len(nums2) + 1) // 2
        
        # 1,3 | 4
        #   2 | 2
        while start <= end:
            mid1 = (start + end) // 2
            mid2 = half_length - mid1
            l1, l2 = self.get_l1_l2(mid1, mid2, nums1, nums2)
            r1, r2 = self.get_r1_r2(mid1, mid2, nums1, nums2)

            if l1 <= r2 and l2 <= r1:
                if (len(nums1) + len(nums2)) & 1 == 0:
                    return (max(l1, l2) + min(r1, r2))/2 
                return max(l1,l2)

            if l1 > r2:
                end = mid1 - 1
            elif l2 > r1:
                start = mid1 + 1

        return 0


    def get_l1_l2(self, mid1, mid2, nums1, nums2):
        
        l1 = -float('inf')
        l2 = -float('inf')

        if mid1 > 0:
            l1 = nums1[mid1 - 1]
            
        if mid2 > 0:
            l2 = nums2[mid2 - 1]
        
        return l1, l2

    
    def get_r1_r2(self, mid1, mid2, nums1, nums2):

        r1 = float('inf')
        r2 = float('inf')

        if mid1 < len(nums1):
            r1 = nums1[mid1]

        if mid2 < len(nums2):
            r2 = nums2[mid2]

        return r1, r2
