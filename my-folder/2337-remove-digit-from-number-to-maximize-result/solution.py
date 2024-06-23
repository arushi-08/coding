class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        
        removeidx = 0
        for i in range(len(number)-1):
            if number[i] == digit:
                if number[i+1] > number[i]:
                    removeidx = i
                    break
                else:
                    removeidx = i
                    
        if not removeidx:
            if number[i+1] == digit:
                removeidx = i + 1 
        
        return number[:removeidx] + number[removeidx+1:]
