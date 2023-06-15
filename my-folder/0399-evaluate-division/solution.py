from collections import defaultdict, deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        # a/b = 2, b/c = 3
        # queries: a/c, b/a, a/e, a/a, x/x

        graph = defaultdict(list)
        for (num, den), val in zip(equations, values):
            graph[num].append([val,den])
            graph[den].append([1/val,num])
        # print(graph)
        def bfs(graph, src, tgt):
            if src not in graph or tgt not in graph: return -1

            queue = deque()
            visit = set()
            queue.append((src, 1))
            visit.add(src)
            while len(queue):
                cursrc, curans = queue.popleft()
                if cursrc == tgt:
                    return curans
                for curwt, curtgt in graph[cursrc]:
                    if curtgt not in visit:
                        visit.add(curtgt)
                        queue.append((curtgt, curans * curwt))
            return -1

        ans = []
        for num, den in queries:
            ans.append(bfs(graph, num, den))

        return ans

