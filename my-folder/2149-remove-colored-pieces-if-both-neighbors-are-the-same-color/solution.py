class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        
        i = 0
        a = 0
        b = 0
        while i+2 < len(colors):
            if colors[i] == colors[i+1] == colors[i+2]:
                if colors[i] == 'A':
                    a += 1
                else:
                    b += 1
            i += 1
        return a>b
        
            
