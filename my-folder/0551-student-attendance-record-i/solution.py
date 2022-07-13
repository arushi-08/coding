class Solution:
    def checkRecord(self, s: str) -> bool:
        
        absent = 0
        late = 0
        for i in s:
            if i == "A": 
                absent += 1
                if absent > 1: return False
                late = 0 
            elif i == "L": 
                late += 1
                if late > 2: return False 
                
            else:
                late = 0
        
        return True
