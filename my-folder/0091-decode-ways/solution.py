class Solution:
    def numDecodings(self, s: str) -> int:
        
        # if s[0] == '0': return 0
        # # backtracking?

        # ans = []
        # def dfs(res, idx):
        #     if idx == len(s):
        #         ans.append(res.copy())
        #         return
            
        #     if s[idx] == '0':
        #         return len(ans)

        #     if idx < len(s) - 1 and int(s[idx:idx+2]) <= 26:
        #         if s[idx+1] == '0':
        #             res.append(s[idx:idx+2])
        #             dfs(res, idx+2)
        #             res.pop()
        #         else:
        #             for i in range(2):
        #                 res.append(s[idx:idx+i+1])
        #                 dfs(res, idx+i+1)
        #                 res.pop()
            
        #     else:
        #         res.append(s[idx])
        #         dfs(res, idx+1)
        #         res.pop()
            
        # res = []
        # dfs(res, 0)
        # # print(ans)
        # return len(ans)
            
            
        # dp problem
        self.memo = {}
        return self.helper(s)
    
    def helper(self, s):
        if s.startswith("0"):
            return 0
        
        if not s or len(s) == 1:
            return 1
        
        if s in self.memo:
            return self.memo[s]

        first = self.helper(s[1:])
        second = 0
        if int(s[0:2]) <= 26:
            second = self.helper(s[2:])

        self.memo[s] = first + second
        return self.memo[s]

