class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        # s1 = 'aabcc'
        # s2 = 'dbbca'
        # s3 = 'aadbbcbcac'

        # if both s1ptr, s2ptr point to same ptr on s3
        # increment both and check what is the next char on s3
        # decrement the ptr on s1/s2, i.e., not matching next char of s3

        # dp method
        self.memo = {}

        def dfs(p1,p2,p3):
            if p1 == len(s1) and p2 == len(s2) and p3 == len(s3):
                return True
            if p3 == len(s3) or (p1 == len(s1) and p2 == len(s2)):
                return False

            if (p1,p2,p3) in self.memo:
                return self.memo[(p1,p2,p3)]

            ans = False
            not_eql = False

            if p1 < len(s1):
                if s1[p1] == s3[p3]:
                    ans |= dfs(p1+1, p2, p3+1)
                else:
                    ans |= False
            if p2 < len(s2):
                if s2[p2] == s3[p3]:
                    ans |= dfs(p1, p2+1, p3+1)
                else:
                    ans |= False

            self.memo[(p1,p2,p3)] = ans
            return ans

        return dfs(0,0,0)
