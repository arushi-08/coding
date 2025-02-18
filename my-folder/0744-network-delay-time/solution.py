class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # times has u to v nodes edge
        # wi = time it takes for a signal to travel from source to target

        # return min time it takes for all n nodes to receive signal

        # heappush all same level nodes

        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((w, v))
        
        heap_nodes = [(0, k)]
        visited = set()
        mintime_graph = {k:0}
        
        while heap_nodes:
            t, k = heappop(heap_nodes)
            for time, nextnode in graph[k]:
                if mintime_graph.get(nextnode, float('inf')) > time+t:
                    heappush(heap_nodes, (time+t, nextnode))
                    mintime_graph[nextnode] = min(
                        time+t, mintime_graph.get(nextnode, float('inf'))
                        )

        if len(mintime_graph) != n:
            return -1
        return max(mintime_graph.values())

# 1->2->3
#  1  2
# 1->3
#  4
