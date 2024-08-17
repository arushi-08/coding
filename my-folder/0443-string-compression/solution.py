class Solution:
    def compress(self, chars: List[str]) -> int:
        
        if len(chars)==1: return 1
        i = 0
        j = 0
        count = 0
        compressed_str = ''
        for j in range(len(chars)):
            if not compressed_str or chars[j] != compressed_str[-1]:
                if count > 1:
                    compressed_str += str(count)
                compressed_str += chars[j]
                count = 1
            else:
                count += 1
        if count > 1:
            compressed_str += str(count)
        
        for j in range(len(compressed_str)):
            chars[j] = compressed_str[j]
        
        return len(compressed_str)

