class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        # there's a directed graph of n nodes
        # 1 node labeled from 0 to n-1
        # graph[i] is nodes adj to node i

        # a node is a terminal node if no outgoing edges
        # a node is safe node if every possible path starting from that node leads to terminal node or another safe node
        # 
        # return array of all safe nodes in graph
        # 
        # basically create a reverse graph and go from terminal node to all previous nodes and store in a list

        # start with terminal
        # create reverse graph
        reverse_graph = defaultdict(list)
        terminal_nodes_queue = deque()
        degree = [0] * len(graph)

        for i, nodes in enumerate(graph):
            degree[i] = len(nodes)
            if not nodes:
                terminal_nodes_queue.append(i)
            
            for connected in nodes:
                reverse_graph[connected].append(i)

        print('reverse_graph', reverse_graph)
        
        terminal_nodes = []
        print(reverse_graph)
        while terminal_nodes_queue:
            curr = terminal_nodes_queue.popleft()
            terminal_nodes.append(curr)

            for neighbor in reverse_graph[curr]:
                degree[neighbor] -= 1
                if degree[neighbor] == 0:
                    terminal_nodes_queue.append(neighbor)

        return sorted(terminal_nodes)
        

        
# problem is  {0: [1], 2: [1], 3: [1, 2], 4: [1, 3]})
# in this q, 1 doesn't have incoming edge, so it doesn't get a key in reverse_graph

        
