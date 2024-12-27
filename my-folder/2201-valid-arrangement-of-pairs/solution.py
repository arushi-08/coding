class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        
        # calculate indegree outdegree and adj list
        # do dfs
        graph = defaultdict(list)
        indegree = defaultdict(int)
        outdegree = defaultdict(int)

        nodes = set()
        for st, ed in pairs:
            graph[st].append(ed)
            indegree[ed] += 1
            outdegree[st] += 1
            nodes.add(ed)
            nodes.add(st)

        # start point
        start = 0
        for node in nodes:
            if outdegree[node] - indegree[node] == 1:
                start = node
                break
        if not start:
            start = node
        # dfs
        def dfs(start, euler_path):
            while outdegree[start]:
                idx = outdegree[start]
                outdegree[start] -= 1
                dfs(graph[start][idx-1], euler_path)

            euler_path.append(start)
        
        euler_path = []
        dfs(start, euler_path)
        euler_path.reverse()
        # print('euler_path', euler_path) 
        ans = []
        for i in range(len(euler_path)-1):
            ans.append([euler_path[i], euler_path[i+1]])
        return ans


