class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []
        def dfs(res, left_count, right_count):
            if len(res)==n*2:
                ans.append(''.join(res))
                return
            
            if left_count < n:
                res.append('(')
                dfs(res, left_count+1, right_count)
                res.pop()
            
            if right_count < left_count:
                res.append(')')
                dfs(res, left_count, right_count+1)
                res.pop()

        dfs([], 0, 0)

        return ans
