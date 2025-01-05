class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        dir_s = [0] * len(s)

        for i in range(len(shifts)):
            st, ed, direction = shifts[i]
            if direction == 0:
                if st > 0:
                    dir_s[st-1] += 1
                dir_s[ed] += -1
            else:
                if st > 0:
                    dir_s[st-1] += -1
                dir_s[ed] += 1
            
        for i in range(len(dir_s)-2,-1,-1):
            dir_s[i] += dir_s[i+1]
        
        s_list = []
        for i in range(len(dir_s)-1,-1,-1):
            s_list.append(chr((ord(s[i]) - ord('a') + dir_s[i])%26+ ord('a')))
        
        return ''.join(s_list[::-1])



