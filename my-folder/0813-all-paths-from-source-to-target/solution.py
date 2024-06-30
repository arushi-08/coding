class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # return all paths from 0 to n-1
        
        hmap = defaultdict(list)
        for st, ed in enumerate(graph):
            hmap[st].extend(ed)

        n = len(graph)
        ans = []
        def dfs(res, ans, idx):
            if idx == n-1:
                ans.append(res.copy())
                return
            
            for i in hmap[idx]:
                res.append(i)
                dfs(res, ans, i)
                res.pop()

        res = [0]
        dfs(res, ans, 0)
        return ans
