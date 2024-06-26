class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        
        # count how many nodes have odd edges
        # if more than 4 -> false
        # else -> can we connect those 4 nodes?

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        odd_nodes = []
        for node in graph:
            if len(graph[node]) & 1:
                odd_nodes.append(node)
        
        print("odd_nodes", odd_nodes)
        if len(odd_nodes) == 0:
            return True
        
        if len(odd_nodes) == 2:
            a, b = odd_nodes
            for i in range(1, n+1):
                if i not in graph[a] and i not in graph[b]:
                    return True
            return False

        if len(odd_nodes) > 4:
            return False

        a, b, c, d = odd_nodes
        # ab cd or ac bd or ad bc
        if (b not in graph[a] and d not in graph[c]) or (c not in graph[a] and d not in graph[b]) or (d not in graph[a] and c not in graph[b]):
            return True

        return False
