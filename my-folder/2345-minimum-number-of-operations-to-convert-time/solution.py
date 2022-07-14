class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        
        moves = [60, 60, 15, 5, 1]
        
        def convert_to_min(time_str):
            hr, minute = time_str.split(":")
            time = int(hr) * 60 + int(minute)
            return time
        
        current = convert_to_min(current)
        correct = convert_to_min(correct)
        
        j = 0
        operations = 0
        while current < correct:
            if current + moves[j] > correct:
                j += 1
            else:
                current += moves[j]
                operations += 1
                
        if current == correct:
            return operations
        return -1
            
            
            
