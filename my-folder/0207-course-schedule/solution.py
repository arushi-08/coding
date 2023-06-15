from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0]*numCourses
        queue = deque()
        visited = set()
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        nodevisited = 0
        while len(queue):
            prereq = queue.popleft()
            nodevisited += 1
            for course in graph[prereq]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)
        
        return nodevisited == numCourses

        




