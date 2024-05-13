class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        ans = []
        comb = {'2':['a','b','c'], 
        '3':['d','e','f'], '4':['g','h','i'],
        '5':['j','k','l'], '6':['m','n','o'],
        '7':['p','q','r','s'], '8':['t','u','v'],
        '9':['w','x','y','z']}

        def dfs(curr, res, ans):
            if not curr:
                if res:
                    ans.append(res)
                return
            
            for digit in comb[curr[0]]:
                res += digit
                dfs(curr[1:], res, ans)
                res = res[:-1]
        
        dfs(digits, '', ans)

        return ans
