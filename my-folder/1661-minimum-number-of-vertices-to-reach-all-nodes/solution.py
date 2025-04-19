class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        in_degree = [0] * n
        for s, e in edges:
            in_degree[e] += 1

        n_vertex = []
        for i in range(n):
            if not in_degree[i]:
                n_vertex.append(i)
        
        return n_vertex


