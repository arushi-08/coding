class Solution:
    def compress(self, chars: List[str]) -> int:
        # iterate 
        # when chars[i] != curr_char
        #   store curr_char and count in chars
        # 

        curr_char = chars[0]
        count = 1
        ptr = 0
        chars += '  '
        for i in range(1, len(chars)):
            if chars[i] != curr_char:
                chars[ptr] = curr_char
                ptr += 1
                if count > 1:
                    for c in str(count):
                        chars[ptr] = c
                        ptr += 1
                    count = 1
                curr_char = chars[i]
            else:
                count += 1
        
        return ptr
