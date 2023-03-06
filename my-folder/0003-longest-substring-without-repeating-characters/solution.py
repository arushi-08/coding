class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        start idx, end idx
        if s[end] not in set -> end += 1
        else: store len(s[start:end]) and start += 1 end += 1
        """
        dist = 0
        chars = set()
        start = 0
        for end in range(len(s)):
            if s[end] not in chars:
                chars.add(s[end])
                dist = max(dist, len(s[start:end+1]))
                # print(s[start:end], s[end], chars)
            elif s[start] == s[end]:
                start += 1
            else:
                # print(s[start:end], s[end], chars)
                # dist = max(dist, len(s[start:end]))
                # # 2 cases either s[end] != s[start] -> start += 1

                # if s[end] not in s[start+1:end]:
                while s[start] != s[end]:
                    chars.remove(s[start])
                    start += 1
                if s[start] == s[end]:
                    start += 1
            end += 1
                
        if not dist:
            dist = len(s[start:])
        return dist
        
