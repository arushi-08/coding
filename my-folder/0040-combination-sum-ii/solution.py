class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        visited = set()
        def dfs(res, idx, n):
            if not n:
                ans.append(res.copy())
                return

            for i in range(idx, len(candidates)):
                if candidates[i] <= n:
                    res.append(candidates[i])
                    if tuple(sorted(res)) not in visited:
                        dfs(res, i+1, n-candidates[i])
                        visited.add(tuple(sorted(res)))
                    res.pop()

        
        dfs([], 0, target)
        return ans
