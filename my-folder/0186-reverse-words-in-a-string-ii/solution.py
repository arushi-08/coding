class Solution:
    def reverse(self, s, i, j):
        while i <= j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

    def reverse_each_word(self, s):
        end_wd = 0
        i = 0
        while i < len(s):
            while end_wd < len(s) and s[end_wd] != ' ':
                end_wd += 1
            self.reverse(s, i, end_wd-1)
            i = end_wd + 1
            end_wd += 1
        

    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverse(s, 0, len(s)-1)
        self.reverse_each_word(s)
