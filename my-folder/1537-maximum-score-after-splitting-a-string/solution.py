class Solution:
    def maxScore(self, s: str) -> int:
        # max score
        # 0's on left + 1's on right
        # 011101
        # prefix sum of 1's
        
        ones = s.count('1')
        zeros = 0
        maxscore = 0
        for i in range(len(s)-1):
            if s[i] == '0':
                zeros += 1
            else:
                ones -= 1
            
            maxscore = max(maxscore, zeros + ones)
        
        return maxscore
            


