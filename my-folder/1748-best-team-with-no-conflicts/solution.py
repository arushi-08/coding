class Solution:
    def sort_scores_n_ages(self, scores, ages):
        sorted_ages = []
        sorted_scores = []
        for a, s in sorted(zip(ages, scores)):
            sorted_ages.append(a)
            sorted_scores.append(s)
        
        return sorted_scores, sorted_ages    
            
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        scores, ages = self.sort_scores_n_ages(scores, ages)
        dp = scores.copy()
        # print(scores, ages)
        for i in range(1, len(scores)):  # 5, 5, 4, 6
            temp = dp[i]
            for j in range(i): # 5
                if scores[i] == scores[j]:
                    temp = max(temp, dp[j]+dp[i])
                elif ages[i] > ages[j] and scores[i] > scores[j]:
                    # print(i, scores[i], dp[j]+dp[i])
                    temp = max(temp, dp[j]+dp[i])
                elif ages[i] == ages[j]:
                    temp = max(temp, dp[j]+dp[i])
            dp[i] = temp
            # print(dp, i)
                
        return max(dp)
            
