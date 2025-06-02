class Solution:
    def romanToInt(self, s: str) -> int:
        
        # 7 symbols
        # number can be < 4, < 9, < 40, < 90
        # 35 - XXXV
        # largest number
        sym_to_int_map = {
            'I':1, 'V':5, 'X':10, 'L':50,
            'C':100, 'D':500, 'M':1000
        }

        num_val = sym_to_int_map[s[0]]

        for i in range(1, len(s)):

            curr_num = sym_to_int_map[s[i]]
            
            if not num_val or sym_to_int_map[s[i-1]] >= curr_num :
                num_val += curr_num
            else:
                num_val += curr_num - 2 * sym_to_int_map[s[i-1]]

        return num_val
        
