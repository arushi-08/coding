class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        
        # maximum bipartite graph matching
        m, n = len(grid), len(grid[0])
        matches = {}

        def dfs(boy, visited):
            "look up match for boy"

            for girl in range(n):

                if grid[boy][girl] and girl not in visited:
                    visited.add(girl)

                    if girl not in matches or dfs(matches[girl], visited):
                        matches[girl] = boy
                        return True
            return False
        
        for boy in range(m):
            dfs(boy, set())
        
        return len(matches)
