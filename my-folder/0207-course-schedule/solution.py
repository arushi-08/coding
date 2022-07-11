from collections import deque
class Solution:
    def count_parents(self, prereq):
        map_dict = {}
        for i in range(len(prereq)):
            map_dict[prereq[i][0]] = map_dict.get(prereq[i][0], 0) + 1
        
        return map_dict
            
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        map_dict = self.count_parents(prerequisites)
        
        queue = deque()
        for course_num in range(numCourses):
            if course_num not in map_dict: queue.append(course_num)
        top_sort = []
        
        while len(queue):
            curr = queue.popleft()
            top_sort.append(curr)
            for i in range(len(prerequisites)):
                if prerequisites[i][1] == curr:
                    map_dict[prerequisites[i][0]] -= 1
                    if map_dict[prerequisites[i][0]] == 0: 
                        queue.append(prerequisites[i][0])
    
        if len(top_sort) == numCourses:
            return True
        return False
                
        
        
