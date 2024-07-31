class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        # have to choose 2 indices
        # have to increment 1 of them, decrement other

        mismatch_nums1 = []
        mismatch_nums2 = []

        for i, j in zip(nums1, nums2):
            if i != j:
                if not k:
                    return -1
                if abs(i - j) % k != 0:
                    return -1
                mismatch_nums1.append(i)
                mismatch_nums2.append(j)
        
        ops = 0
        # 4, 1, 4
        # 1, 7, 1
        subtracts = 0
        adds = 0
        for i in range(len(mismatch_nums1)):

            if mismatch_nums1[i] > mismatch_nums2[i]:
                subtracts += (mismatch_nums1[i] - mismatch_nums2[i]) // k
            else:
                adds += (mismatch_nums2[i] - mismatch_nums1[i]) // k

        if subtracts == adds:
            return subtracts
        
        return -1
