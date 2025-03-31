class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        # n cities

        # given an array flights where flights[i] = [from, to, price]
        # src, dest, k
        # return cheapest price from src to dest
        # with at most k stops


        # return cheapest price from src to dest, constraint k stops

        # either get all paths from src to dest, and reduce number of stops and cost
        # dfs[src][dest][k]?

        # if i do heap method -> doubt - will it complete k stops?
        # get all paths less than k, path = (nodes, cost of path)
        # 

        graph = defaultdict(list)
        for s,d,c in flights:
            graph[s].append((d, c))
        
        self.memo = {}

        def dfs(src, dst, k):
            if src == dst:
                return 0
            
            if k < 0:
                return float('inf')

            if (src, k) in self.memo:
                return self.memo[(src, k)]

            min_cost = float('inf')
            for next_src, cost_to_next in graph[src]:

                min_cost = min(
                    min_cost,
                    dfs(next_src, dst, k-1) + cost_to_next
                )
                
            self.memo[(src, k)] = min_cost
            return min_cost

        min_cost = dfs(src, dst, k)

        if min_cost == float('inf'):
            return -1

        return min_cost
