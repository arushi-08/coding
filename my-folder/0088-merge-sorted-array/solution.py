class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        nums1 < nums2 p1 += 1
        else store nums2 value in nums1 and shift nums1 values by 1  p2 += 1

        """
        p1, p2 = 0, 0
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] <= nums2[p2]:
                p1 += 1
            else:
                i = len(nums1)-1
                while i > p1:
                    nums1[i], nums1[i-1] = nums1[i-1], nums1[i]
                    i -= 1
                nums1[i] = nums2[p2]
                p2 += 1
        p1 = len(nums1)-(len(nums2)-p2)
        if p1 < 0: p1 = 0
        print(p1, p2)
        while p2 < len(nums2):
            nums1[p1] = nums2[p2]
            p2 += 1
            p1 += 1
        return nums1

