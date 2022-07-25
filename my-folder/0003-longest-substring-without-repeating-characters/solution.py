class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        window = defaultdict(int)
        substring_start_idx = 0
        substring_end_idx = 0
        maxlength = 0
        currlength = 0
        # O(N)
        for character in s:
            window[character] += 1
            
            while window[character] > 1:
                window[s[substring_start_idx]] -= 1
                substring_start_idx += 1
                
            maxlength = max(maxlength, substring_end_idx - substring_start_idx + 1)
            
            substring_end_idx += 1
        
        return maxlength
                
