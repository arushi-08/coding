class Solution:
    def __init__(self):
        self.memo = {}

    def minDistance(self, word1: str, word2: str) -> int:
        
        # given 2 strings word1 and word2
        # return min number of ops required to convert word1 into word2
        # insert a character
        # delete a character
        # replace a character
        # dp
        
        # if word1 == word2:
        #     return 0
        
        # if not word1:
        #     return len(word2)
        
        # if not word2:
        #     return len(word1)

        # if (word1, word2) in self.memo:
        #     return self.memo[(word1, word2)]

        # if word1[0] == word2[0]:
        #     ans = self.minDistance(word1[1:], word2[1:])

        # else:
        #     ans = min(
        #         # replace
        #         self.minDistance(word2[0] + word1[1:], word2) + 1,
        #         # insert
        #         self.minDistance(word2[0] + word1, word2) + 1,
        #         # delete
        #         self.minDistance(word1[1:], word2) + 1,
        #     )
        # self.memo[(word1, word2)] = ans
        # return ans

        #   r o s
        # h 
        # o 
        # r 
        # s 
        # e 

        if word1 == word2: return 0

        dp = [[0] * (len(word2)+1) for _ in range( (len(word1)+1) )]

        for i in range(len(word1)+1):
            dp[i][0] = i

        for j in range(len(word2)+1):
            dp[0][j] = j

        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        dp[i-1][j-1],
                        dp[i][j-1],
                        dp[i-1][j]
                    ) + 1

        return dp[len(word1)][len(word2)]
        


        

