class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # sliding window approach
        # 2 ptr: start=0, end=0
        # set of visited chars
        # when we encounter a duplicate
            # increment start till duplicate char index = start
        

        # IMPORTANT :
        # contracting window condn: start should not go till end
        # start should go till 1st s[end] index + 1


        start = 0
        visited_chars = set()
        max_substring_length = 0

        # "abcabcbb"
        # start=0, end=0 | max_substring_length = 1
        # start=0, end=1 | max_substring_length = 2
        # start=0, end=2 | max_substring_length = 3
        # end=3, start=3 | max_substring_length = 3

        # "aab"
        for end in range(len(s)):

            # contracting window
            while s[end] in visited_chars and start < end:
                visited_chars.remove(s[start])
                start += 1
            
            visited_chars.add(s[end])
            max_substring_length = max(max_substring_length, end - start + 1)

        return max_substring_length
