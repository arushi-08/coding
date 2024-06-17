class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        
        line = 1
        limit = 0
        for i in range(len(s)):
            newword = widths[ord(s[i]) - ord('a')]
            if limit + newword > 100:
                line += 1
                limit = newword
            else:
                limit += newword
        
        return [line, limit]

