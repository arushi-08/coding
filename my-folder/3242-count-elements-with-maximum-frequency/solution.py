class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        nmap = Counter(nums)
        maxfreq = max(nmap.values())
        ans = 0
        for k in nmap:
            if nmap[k] == maxfreq:
                ans += nmap[k]
        
        return ans
