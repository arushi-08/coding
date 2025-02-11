class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        #   given s and part
        # perform op on s untill all occurrences of part are removed
        # - find leftmost occurrence of substring part and remove it from s
        # return s after removing all occ
        # 

        s_ptr = 0
        while s_ptr < len(s):
            occurrence_found = False
            while s_ptr < len(s):
                p_ptr = 0

                while s_ptr < len(s) and p_ptr < len(part) and s[s_ptr] == part[p_ptr]:
                    # print('enter', s[s_ptr])
                    p_ptr += 1
                    s_ptr += 1
                    
                # if s_ptr < len(s):
                    # print(p_ptr, s_ptr, s[:s_ptr])
                if p_ptr == len(part):
                    s = s[:s_ptr - p_ptr] + s[s_ptr:]
                    occurrence_found = True
                    break
                elif p_ptr:
                    s_ptr = s_ptr - p_ptr + 1
                else:
                    s_ptr += 1
            # print(s_ptr, occurrence_found, s)
            s_ptr = 0
            if not occurrence_found:
                break

        return s
                
                
