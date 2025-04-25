class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # n pairs of parentheses, generate all
        # ((()))
        """
        n , well-formed
        (((
        i=1

        (
            
        )

        (
        open() (
        close() )

        "(" 
        )/(
        
        """

        results = []

        def dfs(n_open, n_close, curr_result):
            nonlocal n

            if len(curr_result) == 2*n:
                results.append(''.join(curr_result))
                return
            
            if n_open < n:
                dfs(n_open+1, n_close, curr_result + ['('])
            
            if n_open > n_close:
                dfs(n_open, n_close+1, curr_result + [')'] )
            
        
        dfs(1, 0, ['('])
        return results

        # n=3
        # n_open = 1
        # n_open = 2
        # n_open = 3
        # n_close = 1
        # ((()))
        # 
