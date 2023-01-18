from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # min window substring of s so that every char in t
        # including dups is included in window
        # s = "ADOBECODEBANC", t = "ABC"
        #       first get all chars between chars of t
        #      iiiiii, got all chars of t, store local_ans = adobec
        #            iiii, found b another char of t, store local_ans=adobecodeb, 
        #                i, found a another char of t, left_ptr == a, move left_ptr till you get b,(but b is already in window, move left_ptr till next char of t), local_answer = codeba,
        #                 ii, found c another char of t, left_ptr == c, move left_ptr till you get b, local_answer = banc
        i = 0
        j = 0
        freq_t = Counter(t)
        window = {}
        t_counter = 0
        local_answer = s
        global_answer = s
        while j < len(s):
            if s[j] not in freq_t and not window:
                i += 1
                pass
            elif s[j] not in freq_t:
                window[s[j]] = window.get(s[j], 0) + 1
            if s[j] in freq_t:
                window[s[j]] = window.get(s[j], 0) + 1
                if window[s[j]] <= freq_t[s[j]]:
                    t_counter += 1
                # write condn when window doesn't have all freq_t 
                # chars or not all duplicates in freq_t
                # if t_counter != len(t):
                if t_counter == len(t):
                    local_answer = s[i:j+1]
                if s[i] == s[j] and window[s[j]] > freq_t[s[j]]:
                    window[s[i]] -= 1
                    i += 1
                    while (
                        s[i] not in freq_t 
                        or window[s[i]] > freq_t[s[i]]
                        ):
                        window[s[i]] -= 1
                        i += 1
                        local_answer = s[i:j+1]
                        
            j += 1
            if t_counter == len(t):
                global_answer = min((local_answer, global_answer), key=len)

        if global_answer == s and t_counter != len(t): return ''
        return global_answer
                
