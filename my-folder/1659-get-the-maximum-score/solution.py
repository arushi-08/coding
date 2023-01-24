class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:

        # calculate local up and bottom sums, at meeting point check which has greater sum,
        # save greater sum in global answer

        global_answer = 0
        sum1 = 0
        sum2 = 0
        i = 0
        j = 0
        result = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result += max(sum1, sum2) + nums1[i]
                sum1, sum2 = 0, 0
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                sum1 += nums1[i]
                i += 1
            else:
                sum2 += nums2[j]
                j += 1
        while i < len(nums1):
            sum1 += nums1[i]
            i += 1
        while j < len(nums2):
            sum2 += nums2[j]
            j += 1

        return (result + max(sum1, sum2)) % (10**9 + 7)

