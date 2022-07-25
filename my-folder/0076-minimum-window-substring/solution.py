from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # find min substring in s that has all chars of t
        # use freq dictionary of t as window
        
        # keep expanding window by moving right pointer.
        # when window has all desired characters (all T chars), 
        # contract left pointer
        # save smallest window
        
        
        t_freq_dict = Counter(t)
        left_idx = 0
        right_idx = 0
        window = defaultdict(int)
        maxstring = ""
        desired_chars_length = 0 
        
        while right_idx < len(s):
            
            # desired_chars_length = 0
            # keep expanding window by moving right pointer.
            new_char = s[right_idx]
            window[new_char] += 1
            
            if new_char in t_freq_dict and t_freq_dict[new_char] == window[new_char]:
                desired_chars_length += 1
            
            # when window has all desired characters
            if desired_chars_length >= len(t_freq_dict):
                #contract
                old_char = s[left_idx]
                while old_char not in t_freq_dict or window[old_char] > t_freq_dict[old_char]:
                    window[old_char] -= 1
                    
                    if old_char in t_freq_dict and window[old_char] < t_freq_dict[old_char]:
                        desired_chars_length -= 1
                    left_idx += 1
                    old_char = s[left_idx]
                    
                currstring = s[left_idx:right_idx+1]

                if not maxstring:
                    maxstring = currstring
                maxstring = min(maxstring, currstring, key=len)
            

            right_idx += 1
            
        return maxstring
            
