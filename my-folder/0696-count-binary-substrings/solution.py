class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        # group chars
        # 2 insights:
        #   count the min length of groups
        #   this length is the number of substrings
        #   e.g.: '0011', here min group length is 2
        #   that is the num of substrings 01, 0011

        curr = s[0]
        count = 1
        prev = 0
        res = 0
        for i in range(1, len(s)):
            if s[i] == curr:
                count += 1
            else:
                res += min(prev, count)
                curr = s[i]
                prev = count
                count = 1
        res += min(prev, count)
        return res
