from collections import deque, defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        courses_wo_prereqs = [1] * numCourses
        for i in range(len(prerequisites)):
            courses_wo_prereqs[prerequisites[i][0]] = 0
        
        course_graph = defaultdict(list)
        for i in range(len(prerequisites)):
            course_graph[prerequisites[i][0]].append(prerequisites[i][1])

        prereq_graph = defaultdict(list)
        for i in range(len(prerequisites)):
            prereq_graph[prerequisites[i][1]].append(prerequisites[i][0])

        visited = set()
        queue = deque()
        count_courses = 0
        for i in range(len(courses_wo_prereqs)):
            if courses_wo_prereqs[i] == 1:
                queue.append(i)
                visited.add(i)
                count_courses += 1
        print(queue)
        while queue:
            currcourse = queue.popleft()
            for course in prereq_graph[currcourse]:
                if course in visited:
                    continue
                # course - course that has currcourse as prereq
                n_prereqs = 0
                for prereq in course_graph[course]:
                    if prereq in visited:
                        n_prereqs += 1
                    else:
                        break
                if n_prereqs == len(course_graph[course]):
                    queue.append(course)
                    visited.add(course)
                    count_courses += 1
                # print("queue",queue)
        if count_courses == numCourses:
            return True
        return False
            
