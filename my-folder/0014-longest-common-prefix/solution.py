class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # big brain concept:
        # if we sort the list lexicographically,
        #   the first and last strings will have the most difference in prefix

        strs = sorted(strs)
        first_string = strs[0]
        last_string = strs[-1]

        ans = ''
        min_length = min(len(first_string), len(last_string))

        for i in range(min_length):
            if first_string[i] != last_string[i]:
                return ans
            
            ans += first_string[i]
        
        return ans

        

