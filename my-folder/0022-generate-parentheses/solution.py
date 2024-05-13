class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # given n pair of parentheses
        # write function to generate all combinations of well-formed parentheses
        ans = []
        def dfs(left_count, right_count, res):
            if len(res) == n*2: 
                ans.append(''.join(res))
                return
            
            if left_count < n:
                res.append('(')
                dfs(left_count+1, right_count, res)
                res.pop()

            if right_count < left_count:
                res.append(')')
                dfs(left_count, right_count+1, res)
                res.pop()
        
        dfs(0, 0, [])
        return ans
