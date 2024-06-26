class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(list)
        edge = {}
        for e, v in zip(equations, values):
            n, d = e
            graph[n].append(d)
            edge[(n,d)] = v
            graph[d].append(n)
            edge[(d,n)] = 1/v
        
        def dfs(node, ed, visited, edge, graph):
            if node == ed:
                return 1
            
            res = 1
            for nextnode in graph[node]:
                if nextnode not in visited:
                    visited.add(nextnode)
                    res = edge[(node, nextnode)] * dfs(nextnode, ed, visited, edge, graph)
                    if res:
                        return res
                    else:
                        visited.remove(nextnode)
            return 0

        ans = []
        for q in queries:
            st, ed = q
            
            if st == ed:
                if graph[st]:
                    # print("here", st, ed, graph)
                    ans.append(1)
                    continue
                else:
                    ans.append(-1)
                    continue

            visited = set()
            res = dfs(st, ed, visited, edge, graph)
            if res:
                ans.append(res)
            else:
                ans.append(-1)
        
        return ans

            
