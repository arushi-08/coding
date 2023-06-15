from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        indegree = [0] * numCourses
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        queue = deque()
        ans = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
                ans.append(i)
        nodevisited = 0

        while len(queue):
            prereq = queue.popleft()
            nodevisited += 1
            for course in graph[prereq]:
                indegree[course] -= 1
                if indegree[course]==0:
                    queue.append(course)
                    ans.append(course)
        if nodevisited != numCourses: return []
        return ans
            

