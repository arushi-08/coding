from collections import deque
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        # indegree = {node: count of parent nodes}
        # graph = {vertices:[edges]}
        
        indegree = {}
        graph = {}
        
        for i in range(1, n+1):
            indegree[i] = 0
            graph[i] = []
        
        for prereq, next_course in relations:
            indegree[next_course] += 1
            graph[prereq].append(next_course)
            
        queue = deque()
        visited = [False]*(n+1)
        for i in range(1, n+1):
            if indegree[i] == 0:
                queue.append((i, 1))
                visited[i] = True
        
        if not queue:
            return -1
        
        num_semesters = 0
        while queue:
            curr_course, curr_semester = queue.popleft()
            num_semesters = curr_semester
            for next_course in graph[curr_course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0 and visited[next_course] == False:
                    
                    queue.append((next_course, curr_semester + 1))
                    visited[next_course] = True
        
        for idx in range(1, len(visited)):
            if visited[idx] == False:
                return -1
        return num_semesters
            
                
        
