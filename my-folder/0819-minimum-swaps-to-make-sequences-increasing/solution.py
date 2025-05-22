class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        
        # given 2 int arrs
        # 1 op:
        #   swap nums1[i] with nums2[i]
        # make them strictly inc

        # dp
        # when curr elem > next elem
        # swap curr or next?

        # 0,3   2,1
        # 2,3,5,8,9   0,1,4,6,9
        # swaps = 0
        # for i in range(len(nums1)-1):
        #     if nums1[i] >= nums1[i+1] or nums2[i] >= nums2[i+1]:
        #         swaps += 1
        #         if nums1[i] < nums2[i+1] and nums2[i] < nums1[i+1]:
        #             nums1[i+1], nums2[i+1] = nums2[i+1], nums1[i+1]
        
        memo = {}
        def helper(i, swap):
            if i == len(nums1):
                return 0
            if (i, swap) in memo:
                return memo[(i, swap)]

            if swap:
                curr2, curr1 = nums1[i-1], nums2[i-1]
            else:
                curr1, curr2 = nums1[i-1], nums2[i-1]

            best = float('inf')

            if curr1 < nums1[i] and curr2 < nums2[i]:
                best  = min(helper(i+1, 0), best)
            if curr1 < nums2[i] and curr2 < nums1[i]:
                best = min(helper(i+1, 1) + 1, best  )
            memo[(i, swap)] = best

            return memo[(i, swap)]
        
        return min(helper(1,1)+1, helper(1, 0))

        # dp = [[0]]
        # for i in range(len(nums)-2, -1, -1):



