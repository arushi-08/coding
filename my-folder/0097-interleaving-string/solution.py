class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        # s1 = 'aabcc'
        # s2 = 'dbbca'
        # s3 = 'aadbbcbcac'

        # why does greedy not work?
        # s1 = aac
        # s2 = aca
        # s3 = aacaac

        # O(n^2) soln:
        #   nested loop
        '''
        for i -> len(s1):
            for j -> len(s2)
                if we can find s2 in s3
                and compare if the remaining chars form s1
                then True
                else: false
        '''
        if len(s3) != len(s1) + len(s2):
            return False
        

        dp = [[False] * (len(s2)+1) for _ in range(len(s1)+1)]
        dp[-1][-1] = True

        for i in range(len(s1),-1,-1):
            for j in range(len(s2),-1,-1):
                
                if i < len(s1) and s1[i] == s3[i+j] and dp[i+1][j]:
                    dp[i][j] = True
                    continue

                if j < len(s2) and s2[j] == s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True

        return dp[0][0]

