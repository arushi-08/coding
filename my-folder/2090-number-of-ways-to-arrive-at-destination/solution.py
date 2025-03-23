class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        
        # num of ways to go to n-1 intersection in shortest amount of time

        graph = defaultdict(list)

        for u, v, dist in roads:
            graph[u].append((v, dist))
            graph[v].append((u, dist))

        heap = [(0, 0)]
        heapify(heap)

        distance = [float('inf')] * n
        ways = [0] * n
        ways[0] = 1

        MOD = 10**9 + 7

        while heap:
            dist, currnode = heappop(heap)

            if currnode == n-1:
                return ways[currnode] % MOD

            for nextnode, nextdist in graph[currnode]:
                if nextdist + dist < distance[nextnode]:
                    distance[nextnode] = nextdist + dist
                    ways[nextnode] = ways[currnode]
                    heappush(heap, (nextdist+dist, nextnode))
                elif nextdist + dist == distance[nextnode]:
                    ways[nextnode] = (ways[nextnode] + ways[currnode]) % MOD
                    # note: we don't add to heap here
                    # as nextnode is already in heap, we just have found another way to reach nextnode

        return anscount


# I don't need to maintain visited set because we won't revisit a previous node as the distance to traverse back is > than current distance to reach previous node (from node 0).
# we won't traverse back
# 2 states:
# distance and ways
# ways is sum of previous nodes ways when distance is same to reach curr node.


