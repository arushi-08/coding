class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        tokens.sort()
        maxscore = 0
        score = 0
        st = 0
        ed = len(tokens)-1
        while st <= ed:
            if tokens[st] <= power:
                power -= tokens[st]
                score += 1
                st += 1
            elif score:
                power += tokens[ed]
                score -= 1
                ed -= 1
            else:
                break
            maxscore = max(maxscore, score)
            

        return maxscore


