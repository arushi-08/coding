class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        
        # bitwise xor of all pairings - xor of this list
        
        # bitwise of num w itself will give 0
        # even count will be 0
        # odd count will be num itself
        # 1^3, 1^4, 2^3, 2^4
        # 2,1,3 - odd -> so nums2 elems occur odd times
        # 2^10,2^2,2^5,2^0,1^10,1^2,1^5,1^0,3^10,3^2,3^5,3^0
        # 2^10^5
        # 
        m = len(nums1)
        n = len(nums2)
        ans = 0
        if m & 1:
            for num in nums2:
                ans ^= num
        if n & 1:
            for num in nums1:
                ans ^= num
        return ans




