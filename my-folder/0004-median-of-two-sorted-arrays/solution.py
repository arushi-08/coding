class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # find mid point of both n1 and n2
        # n1 = [1,3] | n2 = [2]
        # mid1 = 1  | mid2 = 2
        # 
        
        # compare the 2, if mid1 < mid2
        # search for next mid1 where mid2 can just fit

        # mid1 - do binary search
        # mid2 = len(total)//2 - mid1 = 4 - 1 => 3

        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        half = len(nums1)//2
        if not len(nums2):
            if len(nums1) & 1 == 0:
                return (nums1[half] + nums1[half-1])/2
            return nums1[half]

        total_len = len(nums1) + len(nums2)
        half = (len(nums1) + len(nums2) + 1)//2
        st = 0
        ed = len(nums1)
        print('nums1', nums1)
        print('nums2', nums2)
        while st <= ed:
            mid1 = (st + ed)//2
            mid2 = half - mid1
            print('half', half, 'mid1', mid1)
            print('mid2', mid2)
            l1, r1 = self.helper(nums1, mid1)
            l2, r2 = self.helper(nums2, mid2)
            
            # 1 3 3
            # 4
            # if l1 == -float('inf') or r1 == -float('inf') or l2 == -float('inf'):
            # mid1 - 1, mid2 - 0
            # l1 - -2
            # r2 - inf
            # l2 - 3
            # r1 - -1

            print(
                st, ed, 'mid1',mid1, 'mid2',mid2, 'l1', l1, 'r2',r2, 'l2',l2, 'r1', r1
                )
            # l1 r1
            # l2 r2

            if l1 <= r2 and l2 <= r1:
                if total_len & 1 == 0:
                    return (min(r1,r2) + max(l1,l2))/2
                return max(l1, l2)
            
            if r1 < l2:
                st = mid1 + 1
            elif l1 > r2:
                ed = mid1 - 1
        
        return 0
    
    def helper(self, nums, mid):
        
        l1, r1 = -float('inf'), float('inf')
        print('mid - 1', mid - 1)
        if 0 <= mid - 1 :
            l1 = nums[mid-1]
        if mid < len(nums):
            r1 = nums[mid]
        return l1, r1









