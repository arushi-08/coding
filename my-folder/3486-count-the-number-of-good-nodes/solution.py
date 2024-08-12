class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        def dfs(node, heights, visited):
            nonlocal goodnodes
            if not graph[node]:
                return 0

            size = 1
            good_subtrees = set()
            for child in graph[node]:
                if child not in visited:
                    visited.add(child)
                    size += dfs(child, heights, visited)
                    good_subtrees.add(heights.get(child, 0))

            if len(good_subtrees) == 1 or not good_subtrees:
                goodnodes += 1

            heights[node] = size

            return size

        good_nodes = 0
        heights = defaultdict(int)
        visited = set()
        visited.add(0)
        goodnodes = 0
        # print(graph)
        dfs(0, heights, visited)

        return goodnodes

