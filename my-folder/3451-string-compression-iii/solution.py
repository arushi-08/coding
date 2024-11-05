class Solution:
    def compressedString(self, word: str) -> str:
        
        current = ''
        compressed_str = ''
        count = 0

        for c in word + '_':
            if current and c != current or count == 9:
                compressed_str += str(count) + current
                count = 0

            current = c
            count += 1
        
        return compressed_str


