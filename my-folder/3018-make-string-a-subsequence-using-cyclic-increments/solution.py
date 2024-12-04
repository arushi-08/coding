class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        

        # given 2 0-indexed strings str1, and str2

        # 1 op - select a set of indices in str1 and for each idx i in the set
        # increment str1[i] to the next character cyclically
        # i.e. a becomes b
        # b becomes c

        # return true if it's possible to make str2 a subsequence of str1
        # by perform 1 op

        if len(str2) > len(str1): return False

        j = 0
        for i in range(len(str1)):
            
            if str1[i] == str2[j] or chr(ord(str1[i]) + 1) == str2[j] or (str1[i] == 'z' and str2[j] == 'a'):
                j += 1

            if j == len(str2):
                return True

        return False



