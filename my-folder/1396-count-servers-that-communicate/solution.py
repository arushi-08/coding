class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        n_servers = 0
        rowcount = defaultdict(list)
        colcount = [0] * len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    rowcount[i].append(j)
                    colcount[j] += 1
                    n_servers += 1

        single_server_count = 0
        for i in range(len(grid)):
            if not rowcount[i]: continue
            col_idx = rowcount[i].pop()
            if not rowcount[i] and colcount[col_idx] == 1:
                single_server_count += 1

        return n_servers - single_server_count
