class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        hottest = 0
        for i in range(n-1,-1,-1):
            cur_temp = temperatures[i]
            if cur_temp >= hottest:
                hottest = cur_temp
                continue
            days = 1
            while temperatures[i + days] <= cur_temp:
                days += ans[i + days]
            ans[i] = days
        return ans
