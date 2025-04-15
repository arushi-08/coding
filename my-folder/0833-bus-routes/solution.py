class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        """
        graph nodes -> buses
        find next bus by using stops_to_bus_map{}
            and looping on all buses that go to a stop
        """

        if source == target: return 0

        stops_to_bus_map = defaultdict(list)
        for i in range(len(routes)):
            for stop in routes[i]:
                stops_to_bus_map[stop].append(i)

        queue = deque()
        visited_stops = {source}
        visited_bus = set()
        for bus in stops_to_bus_map[source]:
            queue.append((bus, 1))
            visited_bus.add(bus)
        
        while queue:
            curr, nbuses = queue.popleft()

            if target in routes[curr]:
                return nbuses

            for next_stop in routes[curr]:
                if next_stop not in visited_stops:
                    for next_bus in stops_to_bus_map[next_stop]:
                        if next_bus not in visited_bus:
                            queue.append([next_bus, nbuses+1])
                            visited_bus.add(next_bus)
                    visited_stops.add(next_stop)
        
        return -1

# O(V+E)
# 500 + num of stops intersection
# if all stops are common between 2 buses
# that's still 1 edge
# E = V*(V-1) = V^2?
