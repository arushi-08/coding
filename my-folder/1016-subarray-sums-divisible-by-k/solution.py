class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        # calculate psum array
        # calc diff between immediate psums-store in dict=
        # {remainder/diff:count}
        # apply nC2 formula
        psum = [0]*len(nums)
        psum[0] = nums[0]
        for i in range(1, len(nums)):
            psum[i] = psum[i-1]+nums[i]
        dict1 = {}
        for i in range(len(psum)):
            dict1[psum[i]%k] = dict1.get(psum[i]%k, 0) + 1
        count = 0
        for key, val in dict1.items():
            if key == 0:
                count += val + (val*(val-1)//2)
            else:
                count += (val*(val-1)//2)
        return count


