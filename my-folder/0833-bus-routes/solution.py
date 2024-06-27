class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        if source == target: return 0

        graph = defaultdict(list)
        queue = deque()
        for i, route in enumerate(routes):
            for bustop in route:
                graph[bustop].append(i)
        
        visited = set()
        queue.append(source)

        count = 0
        visited_bustop = set()
        while queue:

            size = len(queue)

            for i in range(size):
                stop = queue.popleft()
                if stop in visited_bustop:
                    continue
                
                visited_bustop.add(stop)
                if stop == target:
                    return count
            
                for bus in graph[stop]:
                    if bus not in visited:
                        visited.add(bus)
                        for nextstop in routes[bus]:
                            queue.append(nextstop)
                        
                
            count += 1

        return -1
