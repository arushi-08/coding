class Solution:
    def validStrings(self, n: int) -> List[str]:
        
        ans = []
        def dfs(res, count):
            if count == 0:
                ans.append(''.join(res))
                return
        
            if res and res[-1] == '0':
                res.append('1')
                dfs(res, count-1)
                res.pop()
            else:
                for i in ['0', '1']:
                    res.append(i)
                    dfs(res, count-1)
                    res.pop()
        
        dfs([], n)
        return ans
