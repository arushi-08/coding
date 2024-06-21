class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        
        seats.sort()
        students.sort()
        minmoves = 0
        for i in range(len(students)):
            minmoves += abs(students[i] - seats[i])
        
        return minmoves

