class Solution:
    def countVowelPermutation(self, n: int) -> int:
        hmap = {
            'a':['e'],
            'e':['a','i'],
            'i':['a','e','o','u'],
            'o':['i','u'],
            'u':['a']
        }
        idx = {'a':0,'e':1,'i':2,'o':3,'u':4}
        dp = [[0] * 5 for _ in range(n)]
        
        for i in range(n):
            for j, char in enumerate(hmap.keys()):
                if i == 0:
                    dp[i][j] = 1
                else:
                    for k, next_char in enumerate(hmap[char]):
                        dp[i][j] += dp[i-1][idx[next_char]]

        # print(dp)
        # print([dp[-1][i] for i in range(5)])
        return sum(dp[-1][i] for i in range(5)) % (10**9 + 7)

    # def countVowelPermutation(self, n: int) -> int:
    #     if n==1:
    #         return 5

    #     self.hmap = {
    #         'a':['e'],
    #         'e':['a','i'],
    #         'i':['a','e','o','u'],
    #         'o':['i','u'],
    #         'u':['a']
    #     }
    #     self.memo = {}
    #     ans = 0
    #     for k in self.hmap:
    #         ans += self.helper(n-1, k)

    #     return ans % (10**9 + 7)

    # def helper(self, n, last_char):
        
    #     if n==1:
    #         return len(self.hmap[last_char])
        
    #     if (n, last_char) in self.memo:
    #         return self.memo[(n, last_char)]

    #     ans = 0
    #     for char in self.hmap[last_char]:
    #         ans += self.helper(n-1, char)
    #     self.memo[(n, last_char)] = ans

    #     return ans

