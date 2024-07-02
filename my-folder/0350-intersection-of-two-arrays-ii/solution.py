class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nmap = Counter(nums1)
        ans = []
        for num in nums2:
            if num in nmap:
                ans.append(num)
                nmap[num] -= 1
                if not nmap[num]:
                    del nmap[num]
        
        return ans
