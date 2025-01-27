class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        graph = defaultdict(list)
        queue = deque()

        dp = [[0]*numCourses for _ in range(numCourses)]

        for p, c in prerequisites:
            dp[c][p] = 1
            graph[c].append(p)
    
        for i in range(numCourses):
            queue.append(i)
            visited = set()
            visited.add(i)

            while queue:
                course = queue.popleft()
                for prereq in graph[course]:
                    if prereq not in visited:
                        queue.append(prereq)
                        dp[i][prereq] = 1
                        visited.add(prereq)
        print(dp)
        ans = []
        for p, c in queries:
            ans.append(dp[c][p]==1)

        return ans

            

