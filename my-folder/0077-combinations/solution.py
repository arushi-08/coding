class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(index, path):
            if len(path) == k:
                res.append(path.copy())
                return
            
            for i in range(index, n+1):
                path.append(i)
                dfs(i+1, path)
                path.pop()
        dfs(1, [])

        return res
            
