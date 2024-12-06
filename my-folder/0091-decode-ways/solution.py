class Solution:
    def numDecodings(self, s: str) -> int:
        
        # return num of ways you can decode string
        # 12
        # 1 -> A
        # 2 -> B
        # 12 -> L
        # backtracking


        # how do we go about it?
        # start at the beginning, select 1 or select 2
        # 2 choices
        # form the result, but 2^100

        # backtracking seems the only option
        # let's start

        memo = {}
        def dfs(i, s):
            if i == len(s):
                return 1
            
            if s[i] == '0':
                return 0

            if i in memo:
                return memo[i]

            res = dfs(i+1, s)
            if s[i] != '0' and i+1 < len(s) and s[i:i+2] < '27':
                res += dfs(i+2, s)
            
            memo[i] = res
            return res

        return dfs(0, s)

