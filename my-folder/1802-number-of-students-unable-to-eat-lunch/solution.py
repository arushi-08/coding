class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        count = 0
        while count < len(students) + 11:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                count = 0
            else:
                st = students.pop(0)
                students.append(st)
                count += 1
            
            if not students:
                return 0

        return len(students)
        



