class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        start = 0
        distinct = 0
        distinctelements = {}
        maxlength = 0
        for end in range(len(s)):

            while distinct > k:
                distinctelements[s[start]] -= 1
                if not distinctelements[s[start]]:
                    del distinctelements[s[start]]
                    distinct -= 1
                start += 1
            
            if s[end] not in distinctelements:
                distinct += 1
            
            distinctelements[s[end]] = distinctelements.get(s[end],0)+1
            # print('distinct', distinct, 'k', k, 'end', end, 'start', start)
            if distinct <= k:
                maxlength = max(maxlength, end-start+1)
    
        return maxlength
