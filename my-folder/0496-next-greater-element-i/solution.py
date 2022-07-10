class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        mapping = {}
        # i = 0
        stack = [nums2[0]]
        for j in range(1, len(nums2)):
            while stack and nums2[j] > stack[-1]:
                mapping[stack.pop()] = nums2[j]
            stack.append(nums2[j])
        
        for i in stack:
            mapping[i] = -1
        
        ans = []
        for i in range(len(nums1)):
            ans.append(mapping[nums1[i]])
        
        return ans
