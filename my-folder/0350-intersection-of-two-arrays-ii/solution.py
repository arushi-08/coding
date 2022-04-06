class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        intersection = []
        ptr2 = 0
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                intersection.append(nums1[i])
                nums2[nums2.index(nums1[i])] = -1
        
        return intersection
