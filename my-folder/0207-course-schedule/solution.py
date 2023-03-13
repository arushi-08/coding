from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topological sort
        # first note all the courses that don't need a prereq course
        # then start with one of these and complete courses those preerqs are done
        prereq_courses = {}
        for i in range(numCourses):
            prereq_courses[i] = 0
        for course_list in prerequisites:
            prereq_courses[course_list[0]] += 1
        
        prereq_courses_inverse = {}
        for i in range(numCourses):
            prereq_courses_inverse[i] = []
        for course_list in prerequisites:
            prereq_courses_inverse[course_list[1]].append(course_list[0])
        
        no_prereq_required = deque()
        for key, val in prereq_courses.items():
            if not val:
                no_prereq_required.append(key)
        done = set()

        while len(no_prereq_required):
            curr = no_prereq_required.popleft()
            done.add(curr)
            for course in prereq_courses_inverse[curr]:
                prereq_courses[course] -= 1
                if course not in done and prereq_courses[course] <= 0:
                    done.add(course)
                    no_prereq_required.append(course)
                    
        if len(done) == numCourses:
            return True
        return False
