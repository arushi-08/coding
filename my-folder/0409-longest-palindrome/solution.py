class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        repeat_elements = {}
        for i in range(len(s)):
            repeat_elements[s[i]] = repeat_elements.get(s[i],0)+1
        
        print(repeat_elements)
        
        is_odd = 0
        ans = 0
        for key in repeat_elements:
            if repeat_elements[key] % 2 == 1:
                # max_odd = max(max_odd, repeat_elements[key])
                ans += repeat_elements[key] - 1
                is_odd = 1
            else:
                ans += repeat_elements[key]
        
        if is_odd:
            return 1 + ans
        return ans
            
            
            
            
