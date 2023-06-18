class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        # brackets = ['(']*n + [')']*n
        # opencount
        def backtrack(opencount, closecount, path):
            if opencount == closecount == n:
                res.append("".join(path))
                return
            
            # for i in range(n):
            if opencount < n:
                path.append('(')
                backtrack(opencount+1, closecount, path)
                path.pop()
            if closecount < opencount:
                path.append(')')
                backtrack(opencount, closecount+1, path)
                path.pop()
        
        backtrack(0, 0, [])
        return res
