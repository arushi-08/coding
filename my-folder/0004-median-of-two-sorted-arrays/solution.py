class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # log n operations
        # binary search
        # heap
        # problem with this question is that 2 arrays will need to interleave

        # only interleave half of array?

        # [1,3] [2,4] - 
        # if len(nums3) < 3
        # 
        i = 0
        j = 0
        nums3 = []
        n1 = len(nums1)
        n2 = len(nums2)
        total_n = n1 + n2
        total_n_half = total_n // 2
        while i < n1 and j < n2 and len(nums3) < total_n_half + 1:
            if nums1[i] < nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1 
        
        while i < n1 and len(nums3) < total_n_half + 1:
            nums3.append(nums1[i])
            i += 1
        
        while j < n2 and len(nums3) < total_n_half + 1:
            nums3.append(nums2[j])
            j += 1

        # print(len(nums3), total_n_half+1)
        if total_n & 1 == 1: # odd
            return nums3[-1]
        
        return (nums3[-2] + nums3[-1])/2
