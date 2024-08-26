class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # dp

        # multiples of 2
        # multiples of 3
        # multiples of 5

        # dp[0] = 1

        # 2 * 1 = 2
        # 3 * 1 = 3
        # 5 * 1 = 5
        # dp[1] = 2 | increment ptr for 2 to 1 from 0

        # 2 * 2 = 4
        # 3 * 1 = 3
        # 5 * 1 = 5
        # dp[2] = 3 | increment ptr for 3 to 1 from 0

        dp = [0, 1]
        ptr_2 = 1
        ptr_3 = 1
        ptr_5 = 1
        # n = 10
        # dp = [0]
        # candidate_2 = 2 | candidate_3 = 3 | candidate_5 = 5
        # dp = [0, 1, 2]
        # candidate_2 = 4 | candidate_3 = 3 | candidate_5 = 5
        # dp = [0, 1, 2, 3]
        
        while len(dp) < (n+1):
            
            candidate_2 = 2 * (dp[ptr_2])
            candidate_3 = 3 * (dp[ptr_3])
            candidate_5 = 5 * (dp[ptr_5])

            if candidate_2 == min(candidate_2, candidate_3, candidate_5):
                dp.append(candidate_2)
                ptr_2 += 1
                if candidate_2 == candidate_3:
                    ptr_3 += 1
                if candidate_2 == candidate_5:
                    ptr_5 += 1
            
            elif candidate_3 == min(candidate_2, candidate_3, candidate_5):
                dp.append(candidate_3)
                ptr_3 += 1
                if candidate_2 == candidate_3:
                    ptr_2 += 1
                if candidate_3 == candidate_5:
                    ptr_5 += 1
            
            else:
                dp.append(candidate_5)
                ptr_5 += 1
                if candidate_2 == candidate_5:
                    ptr_2 += 1
                if candidate_3 == candidate_5:
                    ptr_3 += 1
        
        # print(dp)
        return dp[-1]

        



